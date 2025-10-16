import argparse
from ctfnote import CTFNote
import pathlib
import os
from tabulate import tabulate

def tasks_func(args, ctfnote : CTFNote):
    tasks = ctfnote.getTasks()
    rows = []
    dump_path = args.dump
    if dump_path: os.makedirs(dump_path, exist_ok=True)

    for task in tasks:
        if task.ctf_id != args.ctf_id:
            continue 

        if dump_path:
            filename = f"{'solved - ' if task.solved else ''}{task.title}.md"
            with open(os.path.join(dump_path, filename), 'w') as f:
                f.write(ctfnote.getTaskNotes(task))
                if task.solved: f.write(f"\n> {task.flag}") # print flag at the bottom of the file

            print(f"Dumping {task.title}")

        rows.append([
            task.title
        ])

    print(tabulate(rows, headers=["CTF Id", "Title", "Start Time"]))

def ctfs_func(args, ctfnote : CTFNote):
    ctfs = ctfnote.getCTFs()
    rows = []
    for ctf in ctfs:
        rows.append([
            ctf.id, ctf.title, ctf.start_time
        ])

    print(tabulate(rows, headers=["Tasks"]))

def main():
    args = parser.parse_args()

    ctfnote = CTFNote(base_url=args.url)
    ctfnote.login(user=args.user, passwd=args.password)

    if 'func' in args:
        args.func(args, ctfnote)

parser = argparse.ArgumentParser(
                    prog='ctfnote-cli',
                    description='CTFNote Command Line Interface')

parser.add_argument("--url", required=True, 
                    help="CTFNote Base URL (e.g. https://ctfnote.local")

parser.add_argument("-u", "--user", required=True, 
                    help="CTFNote username")

parser.add_argument("-p", "--password", required=True, 
                    help="CTFNote password")

subparsers = parser.add_subparsers(title='Commands')

ctfs_parser  = subparsers.add_parser('ctfs', description="CTF Commands")
ctfs_parser.set_defaults(func=ctfs_func)


tasks_parser = subparsers.add_parser('tasks', description="Task Commands")
tasks_parser.add_argument("-i", "--ctf-id", required=True, type=int)
tasks_parser.add_argument("--dump", type=pathlib.Path)
tasks_parser.set_defaults(func=tasks_func)


if __name__ == "__main__":
    main()
