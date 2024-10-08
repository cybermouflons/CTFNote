import { connectToDatabase } from "./database";
import { PoolClient } from "pg";
import { createPad } from "../../plugins/createTask";
import { Task } from "./tasks";

export interface CTF {
  id: bigint;
  title: string;
  weight: number;
  ctf_url: string;
  ctf_platform: string;
  logo_url: string;
  ctftime_url: string;
  description: string;
  start_time: Date;
  end_time: Date;
  secrets_id: bigint;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function buildCtf(row: any): CTF {
  return {
    id: row.id as bigint,
    title: row.title as string,
    weight: row.weight as number,
    ctf_url: row.ctf_url as string,
    ctf_platform: row.ctf_platform as string,
    logo_url: row.logo_url as string,
    ctftime_url: row.ctftime_url as string,
    description: row.description as string,
    start_time: row.start_time as Date,
    end_time: row.end_time as Date,
    secrets_id: row.secrets_id as bigint,
  };
}

export async function getCtfSecretsFromDatabase(
  ctfId: bigint,
  pgClient: PoolClient | null = null
): Promise<{
  username: string;
  password: string;
  scoreboardName: string;
  extraInfo: string;
}> {
  const useRequestClient = pgClient != null;
  if (pgClient == null) pgClient = await connectToDatabase();

  try {
    const query = `SELECT username, password, scoreboard_name, extra_info FROM ctfnote.ctf_secrets WHERE id = $1`;
    const values = [ctfId];
    const queryResult = await pgClient.query(query, values);

    return queryResult.rows[0];
  } catch (error) {
    console.error("Failed to fetch CTF secrets from the database:", error);
    return { username: "", password: "", scoreboardName: "", extraInfo: "" };
  } finally {
    if (!useRequestClient) pgClient.release();
  }
}

export async function getCTFNamesFromDatabase(): Promise<string[]> {
  const pgClient = await connectToDatabase();

  try {
    const query = `SELECT title, start_time, end_time
                       FROM ctfnote.ctf
                       WHERE end_time >= NOW()
                       ORDER BY start_time ASC;`;

    const queryResult = await pgClient.query(query);

    return queryResult.rows.map((row) => row.title);
  } catch (error) {
    console.error("Failed to fetch CTF names from the database:", error);
    return [];
  } finally {
    pgClient.release();
  }
}

export async function getAllCtfsFromDatabase(): Promise<string[]> {
  const pgClient = await connectToDatabase();

  try {
    const query = `SELECT title FROM ctfnote.ctf;`;

    const queryResult = await pgClient.query(query);

    return queryResult.rows.map((row) => row.title);
  } catch (error) {
    console.error("Failed to fetch all CTFs from the database:", error);
    return [];
  } finally {
    pgClient.release();
  }
}

// get id from ctf name
export async function getCtfFromDatabase(
  ctfName: string | bigint,
  pgClient: PoolClient | null = null
): Promise<CTF | null> {
  const useRequestClient = pgClient != null;
  if (pgClient == null) pgClient = await connectToDatabase();

  try {
    //make a query to get all the challenges from a ctf

    let query =
      "SELECT id, title, weight, ctf_url, ctf_platform, logo_url, ctftime_url, description, start_time, end_time, secrets_id FROM ctfnote.ctf";

    if (typeof ctfName === "string") {
      query += " WHERE title = $1";
    } else if (typeof ctfName === "bigint" || typeof ctfName === "number") {
      query += " WHERE id = $1";
    } else {
      throw new Error("Invalid type for ctfName: " + typeof ctfName);
    }

    const values = [ctfName];
    const queryResult = await pgClient.query(query, values);

    return buildCtf(queryResult.rows[0]);
  } catch (error) {
    console.error("Failed to get CTF from the database:", error);
    return null;
  } finally {
    if (!useRequestClient) pgClient.release();
  }
}

export async function getNameFromUserId(userId: bigint): Promise<string> {
  const pgClient = await connectToDatabase();

  try {
    const query = "SELECT username FROM ctfnote.profile WHERE id = $1";
    const values = [userId];
    const queryResult = await pgClient.query(query, values);

    return queryResult.rows[0].username;
  } catch (error) {
    console.error("get name from user id from the database:", error);
    return "";
  } finally {
    pgClient.release();
  }
}

export async function createTask(
  title: string,
  description: string,
  tags: string[],
  files: string,
  flag: string,
  padUrl: string,
  ctfId: bigint
): Promise<Task | null> {
  const pgClient = await connectToDatabase();

  try {
    if (!padUrl) {
      padUrl = await createPad(title, description, tags);
    }
    const taskQuery = `
        INSERT INTO ctfnote.task (title, description, files, flag, pad_url, ctf_id)
        VALUES ($1, $2, $3, $4, $5, $6)
        RETURNING id
    `;
    const result = await pgClient.query(taskQuery, [
      title,
      description,
      files,
      flag,
      padUrl,
      ctfId,
    ]);
    const taskId = result.rows[0].id;
    const task = {
      id: taskId,
      tags,
      title,
      description,
      files,
      ctf_id: ctfId,
      flag,
    };
    const tagQuery = `
      WITH insert_tag AS (
        INSERT INTO ctfnote.tag (tag)
        VALUES ($1)
        ON CONFLICT (tag) DO NOTHING
        RETURNING id
      )
      SELECT id FROM insert_tag
      UNION ALL
      SELECT id FROM ctfnote.tag WHERE tag = $1
      LIMIT 1
    `;
    const assignedTagsQuery = `
        INSERT INTO ctfnote.assigned_tags (task_id, tag_id)
        VALUES ($1, $2)
    `;
    const tagValues = tags.map((tag) => [tag]);
    for (const tagValue of tagValues) {
      const result = await pgClient.query(tagQuery, tagValue);
      const tagId = result.rows[0].id;
      await pgClient.query(assignedTagsQuery, [taskId, tagId]);
    }
    return task;
  } catch (error) {
    console.error("Failed to create a task in the database:", error);
    throw error;
  } finally {
    pgClient.release();
  }
}

export async function getAccessibleCTFsForUser(
  userId: bigint,
  pgClient: PoolClient | null = null
): Promise<CTF[]> {
  const useRequestClient = pgClient != null;
  if (pgClient == null) pgClient = await connectToDatabase();

  try {
    const query = `SELECT * FROM ctfnote_private.user_can_play_ctfs($1);`;
    const values = [userId];
    const queryResult = await pgClient.query(query, values);

    return queryResult.rows;
  } catch (error) {
    console.error("Failed to fetch accessible CTFs from the database:", error);
    return [];
  } finally {
    if (!useRequestClient) pgClient.release();
  }
}

// invite the user to play the CTF, but only if they don't have access yet
export async function insertInvitation(
  ctfId: bigint,
  profileId: bigint,
  pgClient: PoolClient | null = null
): Promise<void> {
  const useRequestClient = pgClient != null;
  if (pgClient == null) pgClient = await connectToDatabase();

  const accessibleCTFs = await getAccessibleCTFsForUser(profileId, pgClient);
  if (accessibleCTFs.find((ctf) => ctf.id === ctfId) != null) {
    // already has access
    return;
  }

  try {
    // only insert if the user can't play the CTF
    const query = `INSERT INTO ctfnote.invitation (ctf_id, profile_id) VALUES ($1, $2)`;
    const values = [ctfId, profileId];
    await pgClient.query(query, values);
  } catch (error) {
    console.error("Failed to insert invitation in the database:", error);
    return;
  } finally {
    if (!useRequestClient) pgClient.release();
  }
}

export async function getInvitedUsersByCtf(
  ctfId: bigint,
  pgClient: PoolClient | null = null
): Promise<bigint[]> {
  const useRequestClient = pgClient != null;
  if (pgClient == null) pgClient = await connectToDatabase();

  try {
    const query = `SELECT profile_id FROM ctfnote.invitation WHERE ctf_id = $1`;
    const values = [ctfId];
    const queryResult = await pgClient.query(query, values);

    return queryResult.rows.map((row) => row.profile_id);
  } catch (error) {
    console.error("Failed to get invited users from the database:", error);
    return [];
  } finally {
    if (!useRequestClient) pgClient.release();
  }
}

export async function deleteInvitation(
  ctfId: bigint,
  profileId: bigint,
  pgClient: PoolClient | null = null
): Promise<void> {
  const useRequestClient = pgClient != null;
  if (pgClient == null) pgClient = await connectToDatabase();

  try {
    const query = `DELETE FROM ctfnote.invitation WHERE ctf_id = $1 AND profile_id = $2`;
    const values = [ctfId, profileId];
    await pgClient.query(query, values);
  } catch (error) {
    console.error("Failed to delete invitation from the database:", error);
    return;
  } finally {
    if (!useRequestClient) pgClient.release();
  }
}
