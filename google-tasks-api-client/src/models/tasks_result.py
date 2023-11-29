from dataclasses import dataclass
from task import Task


@dataclass
class TasksResult:
    """ Result of calling the Tasks API https://tasks.googleapis.com/tasks/v1/lists/{tasklist}/tasks endpoint"""
    etag: str
    items: list[Task]
    kind: str
    next_page_token: str
