# ctfnote-cli

Used to interact with CTFNote through the command line.

> Doesn't have too many features now. Importantly though it allows to dump out the markdown documents from all tasks of a ctf

## Usage

```
usage: ctfnote-cli [-h] --url URL -u USER -p PASSWORD {ctfs,tasks} ...

CTFNote Command Line Interface

options:
  -h, --help            show this help message and exit
  --url URL             CTFNote Base URL (e.g. https://ctfnote.local
  -u USER, --user USER  CTFNote username
  -p PASSWORD, --password PASSWORD
                        CTFNote password

Commands:
  {ctfs,tasks}
```

### CTFs

- Lists all CTFs

```
usage: ctfnote-cli ctfs [-h]

CTF Commands

options:
  -h, --help  show this help message and exit
```

### Tasks

- Lists all tasks of a particular CTF
- Allows for dumping all markdown pads to an output directory

```
usage: ctfnote-cli tasks [-h] -i CTF_ID [--dump DUMP]

Task Commands

options:
  -h, --help            show this help message and exit
  -i CTF_ID, --ctf-id CTF_ID
  --dump DUMP
```
