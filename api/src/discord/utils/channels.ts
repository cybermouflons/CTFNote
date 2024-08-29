import {
  CategoryChannel,
  ChannelType,
  Collection,
  CommandInteraction,
  ForumChannel,
  Guild,
  GuildForumTagData,
  PermissionsBitField,
  Role,
  TextChannel,
  ThreadChannel,
  EmbedBuilder,
} from "discord.js";
import {
  CTF,
  getAllCtfsFromDatabase,
  getCtfFromDatabase,
} from "../database/ctfs";
import { getDiscordUsersThatCanPlayCTF } from "../database/users";
import config from "../../config";
import {
  Task,
  getTaskByCtfIdAndNameFromDatabase,
  getTaskFromId,
} from "../database/tasks";
import { sendMessageToChannel } from "./messages";
import {
  isChannelOfCtf,
  isRoleOfCtf,
  isCategoryOfCtf,
  isTaskThreadOf,
} from "./comparison";
import { safeSlugify } from "../../utils/utils";

enum CategoryType {
  NEW,
  STARTED,
  SOLVED,
}

export enum ChannelMovingEvent {
  START,
  UNSOLVED,
  SOLVED,
}

export interface TaskInput {
  ctfId: bigint;
  title: string;
  description: string;
  flag: string;
}

export function categoryName(ctf: CTF) {
  return ctf.title;
}

function findAvailableCategoryName(guild: Guild, ctf: CTF | string) {
  let i = 0;
  const originalName = typeof ctf === "string" ? ctf : ctf.title;
  let name = originalName;
  while (guild.channels.cache.find((channel) => channel.name === name)) {
    i++;
    name = `(${i}) ${originalName}`;
  }
  return name;
}

async function createCategoryChannel(
  guild: Guild,
  name: CTF | string,
  role: Role | null | undefined = null
) {
  if (role == null) {
    role = guild.roles.cache.find((r) => isRoleOfCtf(r, name));
    if (role == null) {
      console.error(`Could not find role for CTF`, name, role);
      return null;
    }
  }

  return guild?.channels.create({
    name: findAvailableCategoryName(guild, name),
    type: ChannelType.GuildCategory,
    permissionOverwrites: [
      // Set permissions for @everyone role (default permissions)
      {
        id: guild.roles.everyone,
        deny: [PermissionsBitField.Flags.ViewChannel], // Deny view permission to @everyone
      },
      // Set permissions for the allowed role
      {
        id: role.id,
        allow: [
          PermissionsBitField.Flags.ViewChannel,
          PermissionsBitField.Flags.SendMessagesInThreads,
        ], // Allow view permission to the allowed role
        deny: [
          PermissionsBitField.Flags.CreatePublicThreads,
          PermissionsBitField.Flags.CreatePrivateThreads,
          PermissionsBitField.Flags.ManageThreads,
        ],
      },
    ],
  });
}

async function createForumChannel(
  guild: Guild,
  name: string,
  category: CategoryChannel
) {
  return guild?.channels.create({
    name: name,
    type: ChannelType.GuildForum,
    parent: category.id,
    availableTags: [
      {
        name: "new",
        emoji: { name: "🆕", id: null },
      },
      {
        name: "started",
        emoji: { name: "⌛", id: null },
      },
      {
        name: "solved",
        emoji: { name: "✅", id: null },
      },
    ],
  });
}

async function createTaskChannel(
  guild: Guild,
  ctf: CTF,
  task: Task,
  type: CategoryType
) {
  const taskName = task.title;

  const challsChannel: ForumChannel = getChallsChannelForCtf(guild, ctf);
  if (challsChannel === null || challsChannel === undefined) return;

  let target_tag: null | string = null;
  if (type === CategoryType.NEW) {
    target_tag = "new";
  } else if (type === CategoryType.STARTED) {
    target_tag = "started";
  } else if (type === CategoryType.SOLVED) {
    target_tag = "solved";
  }

  const tag_id = challsChannel.availableTags.find(
    (tag) => tag.name === target_tag
  )?.id;
  const tagsToApply: string[] = [];
  if (tag_id) {
    tagsToApply.push(tag_id);
  }

  const taskEmbed = new EmbedBuilder()
    .setTitle(`${taskName} (CTFNote link)`)
    .setDescription(
      task.description ? task.description : "No description available"
    )
    .setURL(await getTaskLink(task, ctf))
    .addFields({
      name: "Files/instances",
      value: task.files ? task.files : "No files/instances available",
    });

  console.log("Applying tags", tagsToApply);
  const thread = await challsChannel.threads.create({
    name: taskName,
    message: {
      embeds: [taskEmbed],
    },
    appliedTags: tagsToApply,
  });
  await (await thread?.fetchStarterMessage())?.pin();
  return thread;
}

export async function applyTaskTags(task: Task, guild: Guild) {
  const ctf = await getCtfFromDatabase(task.ctf_id);
  if (ctf == null) return;
  const challsChannel: ForumChannel = getChallsChannelForCtf(guild, ctf);
  if (challsChannel === null || challsChannel === undefined) return;

  const tagsToApply: string[] = [];
  const statusTags = [
    await getTagByName("new", challsChannel),
    await getTagByName("started", challsChannel),
    await getTagByName("solved", challsChannel),
  ];
  // find task thread
  const taskThread = await getTaskThread(guild, task, ctf);
  taskThread?.appliedTags.forEach(async (tag) => {
    if (statusTags.includes(tag)) {
      tagsToApply.push(tag);
    }
  });

  // Create new tags if they don't exist
  const newTags: GuildForumTagData[] = challsChannel.availableTags;
  task.tags?.forEach(async (tag) => {
    const discordTag = challsChannel.availableTags.find((t) => t.name === tag);
    if (!discordTag) {
      newTags.push({ name: tag });
    } else {
      tagsToApply.push(discordTag.id);
    }
  });
  await challsChannel.setAvailableTags(newTags);

  console.log("Applying tags", tagsToApply, "to task", task.title);
  return await taskThread?.setAppliedTags(tagsToApply);
}

export async function createChannelsAndRolesForCtf(guild: Guild, ctf: CTF) {
  const allowedRole = await guild.roles.create({
    name: ctf.title,
    mentionable: true,
  });

  const ctfCategory = await createCategoryChannel(
    guild,
    categoryName(ctf),
    allowedRole
  );
  if (ctfCategory == null) return;

  const ctfChalls = await createForumChannel(guild, "challenges", ctfCategory);
  if (ctfChalls == null) return;

  // create challenges-talk channel
  await guild?.channels.create({
    name: `challenges-talk`,
    type: ChannelType.GuildText,
    parent: ctfCategory?.id,
  });

  // create voice channels for the ctf from the .env file
  const numberOfVoiceChannels: number = config.discord.voiceChannels;

  if (numberOfVoiceChannels > 0) {
    for (let i = 0; i < numberOfVoiceChannels; i++) {
      guild?.channels
        .create({
          name: `voice-${i}`,
          type: ChannelType.GuildVoice,
          parent: ctfCategory.id,
        })
        .catch((err) => {
          console.error("Failed to create one of the voice channels.", err);
        });
    }
  }

  // set correct permissions
  const discordIds: string[] = await getDiscordUsersThatCanPlayCTF(ctf.id);
  discordIds.forEach((discordId) => {
    const member = guild?.members.cache.get(discordId);
    if (member) member.roles.add(allowedRole);
  });
}

export function getChannelCategoriesForCtf(
  guild: Guild,
  ctf: CTF | string
): Collection<string, CategoryChannel> {
  return guild.channels.cache.filter(
    (channel) =>
      channel.type === ChannelType.GuildCategory &&
      isCategoryOfCtf(channel, ctf)
  ) as Collection<string, CategoryChannel>;
}

function getCategoryForCtf(guild: Guild, ctf: CTF) {
  const categories = getChannelCategoriesForCtf(guild, ctf);
  return categories.filter((c) => isCategoryOfCtf(c, categoryName(ctf)));
}

export function getTalkChannelForCtf(guild: Guild, ctf: CTF) {
  return guild.channels.cache.find(
    (channel) =>
      channel.type === ChannelType.GuildText &&
      channel.name === `challenges-talk` &&
      isChannelOfCtf(channel, ctf)
  ) as TextChannel;
}

function getChallsChannelForCtf(guild: Guild, ctf: CTF) {
  return guild.channels.cache.find(
    (channel) =>
      channel.type === ChannelType.GuildForum &&
      channel.name === `challenges` &&
      isChannelOfCtf(channel, ctf)
  ) as ForumChannel;
}

export async function createChannelForTaskInCtf(
  guild: Guild,
  task: Task,
  ctf: CTF | null = null,
  announce = false
) {
  // query CTF if not provided
  if (ctf == null) {
    ctf = await getCtfFromDatabase(task.ctf_id);
    if (ctf == null) return;
  }
  let movingType = CategoryType.NEW;

  if (task.flag != "") {
    movingType = CategoryType.SOLVED;
  }

  return handleCreateAndNotify(guild, task, ctf, movingType, announce);
}

async function getTaskLink(task: Task, ctf: CTF | null = null) {
  if (config.pad.domain == "") return "";

  if (ctf == null) {
    ctf = await getCtfFromDatabase(task.ctf_id);
    if (ctf == null) return "";
  }

  const ssl = config.pad.useSSL == "false" ? "" : "s";

  return `http${ssl}://${config.pad.domain}/#/ctf/${ctf.id}-${safeSlugify(
    ctf.title
  )}/task/${task.id}`;
}

async function handleCreateAndNotify(
  guild: Guild,
  task: Task,
  ctf: CTF,
  type: CategoryType,
  announce = false
) {
  const taskChannel = await createTaskChannel(guild, ctf, task, type);
  if (taskChannel == null) return;

  if (announce)
    await sendMessageToChannel(
      getTalkChannelForCtf(guild, ctf),
      `New task created: ${task.title}`,
      false
    );

  // always apply tags on creation
  applyTaskTags(task, guild);

  return taskChannel;
}

export async function createChannelForNewTask(
  guild: Guild,
  newTask: Task,
  announce = false
) {
  const ctf = await getCtfFromDatabase(newTask.ctf_id);
  if (ctf == null) return;

  let movingType = CategoryType.NEW;

  if (newTask.flag != "") {
    movingType = CategoryType.SOLVED;
  }

  const category = await getCategoryForCtf(guild, ctf);
  if (category == null) {
    console.error(
      "Could not find a non-full category for new task",
      newTask,
      announce
    );
    return;
  }

  return handleCreateAndNotify(guild, newTask, ctf, movingType, announce);
}

export async function getTaskThread(guild: Guild, task: Task, ctf: CTF | null) {
  if (ctf == null) {
    ctf = await getCtfFromDatabase(task.ctf_id);
    if (ctf == null) return null;
  }

  // to get around TypeScript's type system
  const c = ctf;

  const challsChannel = getChallsChannelForCtf(guild, c);
  if (!challsChannel) return null;

  const taskChannel = challsChannel.threads.cache.find((thread) => {
    if (isTaskThreadOf(thread, task)) {
      return thread;
    }
  });

  if (taskChannel == null) return null;
  return taskChannel as ThreadChannel;
}

export async function getTagByName(name: string, channel: ForumChannel) {
  return channel.availableTags.find((tag) => tag.name === name)?.id;
}

export async function getCurrentTaskChannelFromDiscord(
  interaction: CommandInteraction
) {
  if (interaction.channel == null) return null;
  console.log(interaction.channel);

  if (!interaction.channel.isThread()) return null;

  const thread = interaction.channel;

  const category = thread.parent?.parent;
  console.log(category);
  if (category == null) return null;

  const ctf = await getCtfFromDatabase(category.name);
  if (ctf == null) return null;

  const name = thread.name;
  if (name == null) return null;

  const task = await getTaskByCtfIdAndNameFromDatabase(ctf.id, name);
  if (task == null) return null;

  return { ctf: ctf, task: task, channel: interaction.channel };
}

export async function moveChannel(
  guild: Guild,
  task: Task | bigint,
  ctf: CTF | null,
  operation: ChannelMovingEvent
) {
  if (typeof task === "bigint" || typeof task === "number") {
    const t = await getTaskFromId(task);
    if (t == null) return;
    task = t;
  }
  if (ctf == null) {
    ctf = await getCtfFromDatabase(task.ctf_id);
    if (ctf == null) return;
  }
  const taskThread = await getTaskThread(guild, task, ctf);
  if (taskThread == null) {
    console.error("Task channel not found", task, ctf, operation);
    return;
  }

  let newTag: string | null = null;

  if (
    operation === ChannelMovingEvent.START ||
    operation === ChannelMovingEvent.UNSOLVED
  ) {
    newTag = "started";
  } else if (operation === ChannelMovingEvent.SOLVED) {
    newTag = "solved";
  }

  if (newTag == null) return;

  let prevTags = taskThread.appliedTags;
  const stateTags = [
    await getTagByName("new", taskThread.parent as ForumChannel),
    await getTagByName("started", taskThread.parent as ForumChannel),
    await getTagByName("solved", taskThread.parent as ForumChannel),
  ];
  console.log("moving task, previous tags", prevTags);
  console.log("state tags", stateTags);
  prevTags = prevTags.filter((tag) => !stateTags.includes(tag));
  console.log("prevTags after filtering", prevTags);

  const tagId = await getTagByName(newTag, taskThread.parent as ForumChannel);
  console.log("Changing applied tags of task", task.title, "to", tagId);
  if (tagId) {
    prevTags.push(tagId);
    taskThread.setAppliedTags(prevTags);
  }
}
/*
 * Returns the CTF names of all categories that are currently active in the Discord server.
 */
export async function getActiveCtfCategories(guild: Guild): Promise<string[]> {
  const allCtfs = await getAllCtfsFromDatabase();

  return allCtfs.filter((ctf) =>
    guild.channels.cache.find(
      (channel) =>
        channel.type === ChannelType.GuildCategory &&
        isCategoryOfCtf(channel, ctf)
    )
  );
}
