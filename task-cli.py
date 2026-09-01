import argparse
import json
from pathlib import Path
import datetime

tasks = "tasks.json"    # Filname
task_data = {"task": []}    # Defining the structure

if Path(tasks).exists():    # If "tasks.json" exist execute the rest
    with(open(tasks, "r")) as f:
        content = f.read()
        
        if(content):
            task_data = json.loads(content)
            
def save(): # Save functionality
    with(open(tasks, 'w')) as f:
        json.dump(task_data, f, indent=4)


def id_generator(): # Id generator for task
    highest_id = 0
    for i in task_data['task']:
        if(i["id"] > highest_id):
            highest_id = i["id"]
    return highest_id + 1             

def add_task():
    new_id = id_generator()
    now = datetime.datetime.now().isoformat()
    task_data['task'].append({
            "id": new_id,
            "task": args.description,
            "status":  "todo",
            "createdAt": now,
            "updatedAt": now
        })
    save()
    print(f"Task {new_id} added successfully")


def update_task():
    found = False
    for i in task_data['task']:
        if(int(args.id) == i['id']):
            i['task'] = args.description
            i['updatedAt'] = datetime.datetime.now().isoformat()
            found = True
            break
    if(found):
        save()
        print(f"Task {args.id} updated successfully")
    else:
        print(f"ID {args.id} not found")
            
def delete_task():
    found = False
    for i in task_data['task']:
        if(int(args.id) == i['id']):
            task_data['task'].remove(i)
            found = True
            break
    if(found):
        save()
        print(f"Task {args.id} deleted successfully")
    else:
        print(f"ID {args.id} not found")   

def mark_in_progress():
    found = False
    for i in task_data['task']:
        if(args.id) == i['id']:
            i['status'] = "in-progress"
            i['updatedAt'] = datetime.datetime.now().isoformat()
            found = True
            break
    if(found):
        save()
        print(f"Task {args.id} set to in-progress")
    else:
        print(f"ID {args.id} not found")  
        
def mark_done():
    found = False
    for i in task_data['task']:
        if(args.id) == i['id']:
            i['status'] = "done"
            i['updatedAt'] = datetime.datetime.now().isoformat()
            found = True
            break
    if(found):
        save()
        print(f"Task {args.id} Completed")
    else:
        print(f"ID {args.id} not found")

def list_tasks():
    status_filter = args.status 
    for i in task_data['task']:
        if(status_filter is None or i['status'] == status_filter):
            print(f'''Task {i['id']}: {i['task']}
Status: {i['status']}
Created At: {i['createdAt']}
Updated At: {i['updatedAt']}\n''')

# Arguments for cli

parser = argparse.ArgumentParser(prog="task-cli")
subparsers = parser.add_subparsers(dest="command", required=True)

add_parser = subparsers.add_parser("add")
add_parser.add_argument("description")

update_parser = subparsers.add_parser("update")
update_parser.add_argument("id", type=int)
update_parser.add_argument("description")

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id", type=int)

mark_in_progress_parser = subparsers.add_parser("mark-in-progress")
mark_in_progress_parser.add_argument("id", type=int)

mark_done_parser = subparsers.add_parser("mark-done")
mark_done_parser.add_argument("id", type=int)

list_parser = subparsers.add_parser("list")
list_parser.add_argument("status", nargs="?", choices=["done", "todo", "in-progress"], default=None)

args = parser.parse_args()

commands = {
    "add": add_task,
    "update": update_task,
    "delete": delete_task,
    "mark-in-progress": mark_in_progress,
    "mark-done": mark_done,
    "list": list_tasks
}

commands[args.command]()