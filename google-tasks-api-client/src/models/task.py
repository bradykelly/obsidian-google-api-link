from dataclasses import dataclass
from datetime import datetime
from task_link import TaskLink


@dataclass
class Task:
    """ Result of calling the Tasks API https://tasks.googleapis.com/tasks/v1/lists/{tasklist}/tasks/{task} endpoint """
    kind: str
    id: str
    title: str
    status: str
    notes: str
    parent: str
    position: int
    completed: str
    deleted: bool
    due: datetime
    etag: str
    hidden: bool
    selfLink: str
    updated: datetime
    links: list[TaskLink]

    def __repr__(self):
        return '<Task %r>' % self.title