import {
  Client,
  CommandInteraction,
  TextChannel,
  ApplicationCommandType,
  ApplicationCommandOptionType,
  PermissionFlagsBits,
} from "discord.js";
import { Command } from "../command";
import { getCtfFromDatabase, createTask } from "../database/ctfs";
import { createPad } from "../../plugins/createTask";
import { sendMessageToChannel } from "../utils/messages";
import {
  createChannelForNewTask,
  getTalkChannelForCtf,
} from "../utils/channels";
import { getTaskByCtfIdAndNameFromDatabase } from "../database/tasks";

async function addTaskLogic(client: Client, interaction: CommandInteraction) {
  const channel = interaction.channel;

  if (channel && channel instanceof TextChannel && channel.parent) {
    const category = channel.parent;

    if (!category) {
      await interaction.editReply({
        content:
          "Ρε για να μπόρεις να προσθέσεις τσαλ πρέπει να είσαι σε CTF talk channel!",
      });
      return;
    }

    const ctfName = category.name;
    const ctf = await getCtfFromDatabase(ctfName);
    if (ctf == null) {
      await interaction.editReply({
        content:
          "Ρε για να μπόρεις να προσθέσεις τσαλ πρέπει να είσαι σε CTF talk channel!",
      });
      return;
    }

    const title = interaction.options.get("title", true).value as string;
    const tags = interaction.options.get("tags", true).value as string;
    const tagsArray = tags.split(" ");
    const padUrl = await createPad(title, "", tagsArray);
    try {
      await createTask(title, "", "", "", padUrl, ctf.id);
    } catch (e) {
      await interaction.editReply({
        content: "Κατι επίεν στραβά και εν εκατάφερα να κάμω το τσαλ.",
      });
      return;
    }

    const task = await getTaskByCtfIdAndNameFromDatabase(ctf.id, title);
    if (task == null) {
      await interaction.editReply({
        content: "Κατι επίεν στραβά και εν εκατάφερα να κάμω το τσαλ.",
      });
      return;
    }
    const guild = interaction.guild;
    if (guild == null) return;

    const taskThread = await createChannelForNewTask(guild, task);
    const talkChannel = getTalkChannelForCtf(guild, ctf);
    await sendMessageToChannel(
      talkChannel,
      `Έκαμα το τσαλ ${taskThread} να δούμε ποιος θα το λύσει!`
    );
    await interaction.editReply({
      content: `'Εκαμα το τσαλ!'`,
    });
    return;
  } else {
    await interaction.editReply({
      content:
        "This command can only be used in a text channel within a category.",
    });
    return;
  }
}

export const AddTask: Command = {
  name: "addchall",
  description: "Create a new task for the CTF.",
  type: ApplicationCommandType.ChatInput,
  defaultMemberPermissions: [PermissionFlagsBits.Administrator],
  options: [
    {
      name: "title",
      required: true,
      description: "The challenge title",
      type: ApplicationCommandOptionType.String,
      minLength: 1,
    },
    {
      name: "tags",
      required: true,
      description: "The tags of the challenge as a space-separated string",
      type: ApplicationCommandOptionType.String,
    },
  ],
  run: async (client: Client, interaction: CommandInteraction) => {
    try {
      await addTaskLogic(client, interaction);
    } catch (e) {
      console.error("Error during addTask logic: ", e);
      if (!interaction.replied && !interaction.deferred) {
        await interaction.editReply({
          content: "An error occurred while processing your request.",
        });
      }
    }
  },
};
