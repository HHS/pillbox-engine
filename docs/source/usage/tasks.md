Pillbox Engine runs many backgound tasks. It relies on [Celery](http://www.celeryproject.org) to execute and manage background tasks.

### One Task at a time

Because Pillbox Engine's tasks are long intensive processes, we have limited concurrent tasks to only one. The system is designed to run only one task at a time. There task table that shows the status of all tasks, active, failed, canceled or in progress.

![tasks](../img/tasks.png)

When you click on each task, you can view more information about the task.

### Cancel a Task

If there is a running task, you always can stop the task by selecting the active task and click on the action as shown below:

![cancel_task](../img/cancel_task.gif)

### Task Types

Some of the tasks are intensive and should only be run once every 24 hours as the data gets updated every 24 hours. The engine enforces the limit.

This is the list of all tasks and associated limits

- download (every 24 hours for each source)
- products (every 24 hours)
- pills (every 24 hours)
- import (no limit)
- compare (every 24 hours)
- export (no limit)

You can always overwrite the limit by deleting the the most recent task record. For example if you want to redownload HOTC that was downloaded in hour ago, go to the tasks list, find the download task for the latest HOTC download and delete it. This will overwrite the limit and allow you to re-run the task.

### Starting a Task and Checking the Progress

You can start most tasks by going to [main dashboard (home)](http://localhost:5000/) and click on the relevant action box.

For example to start an ANIMAL download, click on the ANIMAL action box. If you click again on the action box, you will see the progress of the action.

If an action has an execution limit, it does not start. If an action running, the other actions do not start.

![task progress](../img/task_progress.gif)



