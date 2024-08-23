CREATE TABLE ctfnote.ctf_secrets (
  id serial PRIMARY KEY,
  username text,
  password text,
  scoreboard_name text,
  extra_info text
);

GRANT SELECT ON ctfnote.ctf_secrets TO user_guest;

GRANT UPDATE (username) ON ctfnote.ctf_secrets TO user_manager;
GRANT UPDATE (password) ON ctfnote.ctf_secrets TO user_manager;
GRANT UPDATE (scoreboard_name) ON ctfnote.ctf_secrets TO user_manager;
GRANT UPDATE (extra_info) ON ctfnote.ctf_secrets TO user_manager;
