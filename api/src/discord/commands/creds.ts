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

  if (channel && channel instanceof TextChannel && channel.parent) {
    const category = channel.parent;

    if (!category) {
      await interaction.editReply({
        content:
          "Ρε για να σου έβρω τα creds πρέπει να είσαι σε CTF talk channel!",
      });
      return;
    }

    const ctfName = category.name;
    const ctf = await getCtfFromDatabase(ctfName);
    if (ctf == null) {
      await interaction.editReply({
        content:
          "Ρε για να σου έβρω τα creds πρέπει να είσαι σε CTF talk channel!",
      });
      return;
    }

    const secrets = await getCtfSecretsFromDatabase(ctf.id);
    if (!secrets) {
      await interaction.editReply({
        content: "Πού θέλεις να τα έβρω εγώ; 'Εδωκες μου τα ποτέ;",
      });
      return;
    }

    const markdown = `# CTF Secrets
    Username: ${secrets.username ?? "No username found"}
    Password: ${secrets.password ?? "No password found"}
    Scoreboard name: ${secrets.scoreboardName ?? "No scoreboard name found"}
    Extra info: ${secrets.extraInfo ?? "No extra info found"}`;

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
