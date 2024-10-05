import { ApplicationCommandType, Client, CommandInteraction } from "discord.js";
import { Command } from "../command";
import {
  userStartsWorkingOnTask,
  userStopsWorkingOnTask,
} from "../database/tasks";
import {
  sendStartWorkingOnMessage,
  sendStopWorkingOnMessage,
} from "../../plugins/discordHooks";
import { getUserByDiscordId } from "../database/users";
import { getCurrentTaskChannelFromDiscord } from "../utils/channels";

async function accessDenied(interaction: CommandInteraction) {
  await interaction.editReply({
    content:
      "You are not using a valid channel to start/stop working on the task",
  });
}

async function workingOnLogic(
  _client: Client,
  interaction: CommandInteraction,
  operation: "start" | "stop"
) {
  const guild = interaction.guild;
  if (guild == null) return;

  const result = await getCurrentTaskChannelFromDiscord(interaction);
  if (result == null) return accessDenied(interaction);

  const task = result.task;

  const userId = interaction.user.id;
  const userExistsOnCtfNote = await getUserByDiscordId(userId);
  //   const userId = await getUserByDiscordId(interaction.user.id);
  //   if (userId == null) {
  //     await interaction.editReply({
  //       content:
  //         "You have not linked your CTFNote account to your Discord account yet. Please use the /link command to do so.",
  //     });
  //     return;
  //   }

  if (operation === "start") {
    let result = false;
    if(userExistsOnCtfNote !== null){
      result = await userStartsWorkingOnTask(userExistsOnCtfNote, task.id);
    }
    if (userExistsOnCtfNote === null || result) {
      await sendStartWorkingOnMessage(guild, userId, task);
      await interaction.editReply({
        content: `Δώστου πίεση!!`,
      });
      return;
    } else {
      await interaction.editReply({
        content: `Μα ίντα που μου λαλείς ρε αφού υποτίθεται μάσιεσε δαπάνω...`,
      });
      return;
    }
  } else if (operation === "stop") {
    let result = false;
    if(userExistsOnCtfNote !== null){
      result = await userStopsWorkingOnTask(userExistsOnCtfNote, task.id);
    }
    if (result) {
      await interaction.editReply({
        content: `'Ατε έφκαλα σε που δαμέσα πίενε δε κανέναν αλλο τσαλ`,
      });
      await sendStopWorkingOnMessage(guild, userId, task);
      return;
    } else {
      await interaction.editReply({
        content: `Ακόμα εν άρκεψες θέλεις να παραιτήσεις μάνι μάνι`,
      });
      return;
    }
  }
}

export const StartWorking: Command = {
  name: "start",
  description: "Start working on the task linked to this text channel",
  type: ApplicationCommandType.ChatInput,
  run: async (client, interaction) => {
    return workingOnLogic(client, interaction, "start").catch((e) => {
      console.error("Error during start working logic: ", e);
    });
  },
};

export const StopWorking: Command = {
  name: "stop",
  description: "Stop working on the task linked to this text channel",
  type: ApplicationCommandType.ChatInput,
  run: async (client, interaction) => {
    return workingOnLogic(client, interaction, "stop").catch((e) => {
      console.error("Error during stop working logic: ", e);
    });
  },
};
