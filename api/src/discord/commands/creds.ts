import {
  Client,
  CommandInteraction,
  TextChannel,
  ApplicationCommandType,
  PermissionFlagsBits,
} from "discord.js";
import { Command } from "../command";
import {
  getCtfSecretsFromDatabase,
  getCtfFromDatabase,
} from "../database/ctfs";

async function credsLogic(client: Client, interaction: CommandInteraction) {
  const channel = interaction.channel;

  // Check if the channel is a TextChannel and has a parent
  if (channel && channel instanceof TextChannel && channel.parent) {
    const category = channel.parent;

    // Ensure that the category is not null
    if (!category) {
      await interaction.editReply({
        content:
          "This command can only be used in a text channel within a category.",
      });
      return;
    }

    // TODO: Fix after forum implementation
    const ctfName = category.name.split(" - ")[1];
    console.log("CTF Name: ", ctfName);
    const ctf = await getCtfFromDatabase(ctfName);
    if (ctf == null) {
      await interaction.editReply({
        content: "CTF not found!",
      });
      return;
    }
    console.log("CTF: ", ctf);

    // Fetch secrets using CTF ID
    const secrets = await getCtfSecretsFromDatabase(ctf.id);
    if (!secrets || secrets.length === 0) {
      await interaction.editReply({
        content: "No secrets found!",
      });
      return;
    }

    let markdown = "# CTF Secrets\n";
    secrets.forEach((secret) => {
      markdown += `- **Username**: ${secret.username}\n`;
      markdown += `- **Password**: ${secret.password}\n`;
      markdown += `- **Scoreboard Name**: ${secret.scoreboardName}\n\n`;
    });

    await interaction.editReply({
      content: markdown,
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

export const Creds: Command = {
  name: "creds",
  description: "Fetches and sends the CTF secrets in markdown format",
  type: ApplicationCommandType.ChatInput,
  defaultMemberPermissions: [PermissionFlagsBits.Administrator],
  run: async (client: Client, interaction: CommandInteraction) => {
    try {
      await credsLogic(client, interaction);
    } catch (e) {
      console.error("Error during creds logic: ", e);
      if (!interaction.replied && !interaction.deferred) {
        await interaction.editReply({
          content: "An error occurred while processing your request.",
        });
      }
    }
  },
};
