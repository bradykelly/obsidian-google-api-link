from dataclasses import dataclass
from task import Task


@dataclass
class TasksResult:
    etag: str
    items: list[Task]
    kind: str
    next_page_token: str
