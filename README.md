# Task Tracker CLI

A simple command-line tool to track and manage your to-do list. Built as a solution to the [Task Tracker](https://roadmap.sh/projects/task-tracker) project from roadmap.sh.

Tasks are stored in a `tasks.json` file in the current directory, which is created automatically the first time you add a task. No external libraries or frameworks are used — only Python's standard library (`argparse`, `json`, `pathlib`, `datetime`).

## Requirements

- Python 3.7+

No installation or dependencies needed.

## Usage

Run the script with `python task-cli.py <command> [arguments]`.

### Add a task

```bash
python task-cli.py add "Buy groceries"
# Task 1 added successfully
```

### Update a task

```bash
python task-cli.py update 1 "Buy groceries and cook dinner"
# Task 1 updated successfully
```

### Delete a task

```bash
python task-cli.py delete 1
# Task 1 deleted successfully
```

### Mark a task as in progress or done

```bash
python task-cli.py mark-in-progress 1
# Task 1 set to in-progress

python task-cli.py mark-done 1
# Task 1 Completed
```

### List tasks

```bash
python task-cli.py list              # all tasks
python task-cli.py list todo         # only todo
python task-cli.py list in-progress  # only in-progress
python task-cli.py list done         # only done
```

## Task properties

Each task stored in `tasks.json` has:

| Field       | Description                                  |
|-------------|-----------------------------------------------|
| `id`        | Unique, auto-incrementing identifier          |
| `task`      | Description of the task                       |
| `status`    | One of `todo`, `in-progress`, `done`          |
| `createdAt` | ISO 8601 timestamp set when the task is added |
| `updatedAt` | ISO 8601 timestamp, refreshed on any update or status change |

## Example session

```bash
$ python task-cli.py add "Buy groceries"
Task 1 added successfully

$ python task-cli.py add "Feed the dog"
Task 2 added successfully

$ python task-cli.py update 1 "Buy milk"
Task 1 updated successfully

$ python task-cli.py mark-done 1
Task 1 Completed

$ python task-cli.py mark-in-progress 2
Task 2 set to in-progress

$ python task-cli.py list
Task 1: Buy milk
Status: done
Created At: 2026-09-01T11:47:03.598589
Updated At: 2026-09-01T11:48:08.214309

Task 2: Feed the dog
Status: in-progress
Created At: 2026-09-01T11:47:12.098040
Updated At: 2026-09-01T11:48:35.683693
```

## Notes

- Task IDs are not reused after deletion — the next added task always gets `highest existing ID + 1`.
- Invalid input (a non-numeric ID, a missing required argument) produces a standard argparse usage error rather than crashing.
- `tasks.json` is created automatically on first use and is excluded from version control via `.gitignore`, since it holds per-user runtime data rather than source code.
