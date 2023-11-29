from dataclasses import dataclass
from src.models.task_list import TaskList


@dataclass
class TaskListsResult:
    """ Result of calling the tasks API GET https://tasks.googleapis.com/tasks/v1/users/@me/lists endpoint """
    etag: str
    items: list[TaskList]
    kind: str
    next_page_token: str
