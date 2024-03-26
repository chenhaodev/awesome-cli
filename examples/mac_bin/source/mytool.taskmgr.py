import argparse
import os
import json
import datetime
from dateutil.relativedelta import relativedelta
from argparse import RawTextHelpFormatter
import uuid
import sys

#TASK_FILE = "tasks.json"
#TASK_FILE = os.getcwd() + "/../doc/tasks.json"
TASK_FILE = os.environ.get('MACPATH') + "/../doc/tasks.json"

def create_task(args):
    task = {"id": len(get_tasks()) + 1, "description": "["+str(uuid.uuid4())[:4] +"] "+args.description, "completed": False, "tags": [], "reminder": []}
    tasks = get_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Created task: {task['id']:>4}\t{task['description']:<20}")

#def list_tasks(args):
#    tasks = get_tasks()
#    print("ID\tDescription\t\tCompleted\tTags\t\tRemind Date")
#    for task in tasks:
#        completed = "Done" if task["completed"] else " "
#        tags = ", ".join(task["tags"])
#        reminders = ", ".join(task["reminder"])
#        print(f"{task['id']}\t{task['description']:<20}\t{completed}\t{tags:>14}\t{reminders:>18}")

def list_tasks(args):
    tasks = get_tasks()
    print("ID\tStatus\tRemind\t\tTags\tDescription")
    for task in tasks:
        completed = "Done" if task["completed"] else " "
        tags = ", ".join(task["tags"])
        reminders = ", ".join(task["reminder"])
        print(f"{task['id']}\t{completed}\t{reminders:<14}\t{tags}\t{task['description']}")

def complete_task(args):
    tasks = get_tasks()
    task = next((t for t in tasks if t["id"] == args.task_id), None)
    if task:
        task["completed"] = True
        save_tasks(tasks)
        print(f"Completed task: {task['id']:>4}\t{task['description']:<20}")
    else:
        print(f"Task {args.task_id} not found.")

def delete_task(args):
    tasks = get_tasks()
    task = next((t for t in tasks if t["id"] == args.task_id), None)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Deleted task: {task['id']:>4}\t{task['description']:<20}")
    else:
        print(f"Task {args.task_id} not found.")

def add_tags(args):
    tasks = get_tasks()
    task = next((t for t in tasks if t["id"] == args.task_id), None)
    if task:
        task["tags"].extend(args.tags)
        save_tasks(tasks)
        print(f"Added tags to task {task['id']:>4}: {', '.join(args.tags)}")
    else:
        print(f"Task {args.task_id} not found.")

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f)

def get_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

def set_reminder(args):
    tasks = get_tasks()
    task = next((t for t in tasks if t["id"] == args.task_id), None)
    if task:
        if args.reminder.startswith("+"):
            reminder = calculate_relative_date(args.reminder)
        else:
            reminder = args.reminder
        task["reminder"].append(reminder)
        save_tasks(tasks)
        print(f"Set reminder for task {task['id']:>4}: {reminder}")
    else:
        print(f"Task {args.task_id} not found.")

def calculate_relative_date(reminder):
    today = datetime.date.today()
    if reminder.startswith("+") and len(reminder) > 1:
        operator = reminder[0]
        value = reminder[1:]
        if operator == "+":
            if value.endswith("w"):
                weeks = int(value[:-1])
                new_date = today + relativedelta(weeks=weeks)
            else:
                days = int(value)
                new_date = today + datetime.timedelta(days=days)
            return new_date.strftime("%Y-%m-%d")
    return None

def check_reminders():
    tasks = get_tasks()
    today = datetime.date.today()
    for task in tasks:
        reminders = task.get("reminder")
        if reminders:
            for reminder in reminders:
                reminder_date = datetime.datetime.strptime(reminder, "%Y-%m-%d").date()
                if today == reminder_date:
                    print(f"Reminder: Task {task['id']:>4}\t{task['description']:<20}")
    

helptext = "A simple task manager CLI."
parser = argparse.ArgumentParser(prog="<cmd>", description=helptext, formatter_class=RawTextHelpFormatter)
subparsers = parser.add_subparsers(title="subcommands", dest="subcommand", required=True)

create_parser = subparsers.add_parser("new", help="Create a new task.")
create_parser.add_argument("description", help="Task description.")

list_parser = subparsers.add_parser("list", help="List all tasks.")

complete_parser = subparsers.add_parser("complete", help="Complete a task.")
complete_parser.add_argument("task_id", type=int, help="Task ID.")

delete_parser = subparsers.add_parser("remove", help="Remove a task.")
delete_parser.add_argument("task_id", type=int, help="Task ID.")

tags_parser = subparsers.add_parser("tags", help="Add tags to a task.")
tags_parser.add_argument("task_id", type=int, help="Task ID.")
tags_parser.add_argument("tags", nargs="+", help="Tags to add.")

reminder_parser = subparsers.add_parser("reminder", help="Set a reminder for a task.")
reminder_parser.add_argument("task_id", type=int, help="Task ID.")
reminder_parser.add_argument("reminder", help="Reminder date (YYYY-MM-DD or +x days/weeks).")

check_parser = subparsers.add_parser("check", help="Check for reminders.")

args = parser.parse_args()

if args.subcommand == "new":
    create_task(args)
elif args.subcommand == "list":
    list_tasks(args)
elif args.subcommand == "complete":
    complete_task(args)
elif args.subcommand == "remove":
    delete_task(args)
elif args.subcommand == "tags":
    add_tags(args)
elif args.subcommand == "reminder":
    set_reminder(args)
elif args.subcommand == "check":
    check_reminders()
