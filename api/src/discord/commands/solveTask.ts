import {
  ApplicationCommandOptionType,
  ApplicationCommandType,
  CommandInteraction,
} from "discord.js";
import { Command } from "../command";
import { setFlagForChallengeId } from "../database/tasks";
import {
  convertToUsernameFormat,
  handleTaskSolved,
} from "../../plugins/discordHooks";
import { getUserByDiscordId } from "../database/users";
import { getCurrentTaskChannelFromDiscord } from "../utils/channels";

async function accessDenied(interaction: CommandInteraction) {
  await interaction.editReply({
    content: "You are not using a valid channel to solve the task",
  });
}

async function solveTaskLogic(interaction: CommandInteraction) {
  const r = await getCurrentTaskChannelFromDiscord(interaction);
  if (r == null) return accessDenied(interaction);

  const task = r.task;

  const flag = interaction.options.get("flag", true).value as string;
  const solversArray: string[] = [interaction.user.id];
  const solversOption = interaction.options.get("solvers", false);
  if (solversOption && typeof solversOption.value === "string") {
    solversArray.push(
      ...solversOption.value.split(" ").map((s: string) => s.trim())
    );
  }

  if (!flag) return accessDenied(interaction);

  const result = await setFlagForChallengeId(task.id, flag);
  if (result) {
    await interaction.editReply({
      content: `Task solved!`
    });
    const userIdArray = Array.isArray(solversArray)
      ? solversArray
      : [solversArray];
    const userNames = await Promise.all(
      userIdArray.map(async (userId) => convertToUsernameFormat(userId))
    );
    const usernamesString = userNames.join(" ");

    await interaction.followUp({
      ephemeral: false,
      content: `Είσαστε φοθκιά :fire: :fire: :fire: ${usernamesString}`,
    });

    let userId: bigint | null | string = await getUserByDiscordId(
      interaction.user.id
    );
    if (userId == null) userId = interaction.user.id;

    const guild = interaction.guild;
    if (guild == null) return;

    await handleTaskSolved(guild, task.id, solversArray).catch((e) => {
      console.error("Error while handling task solved: ", e);
    });
    return;
  } else {
    await interaction.editReply({
      content: "Task is already solved. Please change the flag in CTFNote.",
    });
  }
}

export const SolveTask: Command = {
  name: "solve",
  description: "Solve the task linked to this text channel",
  type: ApplicationCommandType.ChatInput,
  options: [
    {
      name: "flag",
      required: true,
      description: "The flag to submit to CTFNote",
      type: ApplicationCommandOptionType.String,
      minLength: 1,
    },
    {
      name: "solvers",
      required: false,
      description: "Users assigned as solvers",
      type: ApplicationCommandOptionType.String,
    },
  ],
  run: async (_, interaction) => {
    return solveTaskLogic(interaction).catch((e) => {
      console.error("Error during solve task logic: ", e);
    });
  },
};
