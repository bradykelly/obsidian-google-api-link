from dataclasses import dataclass


@dataclass
class TaskListsResult:
    etag: str
    items: list[]
    kind: str
    next_page_token: str
