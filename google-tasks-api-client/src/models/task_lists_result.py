from dataclasses import dataclass
from marshmallow import Schema, fields, post_load
from models.task_list import TaskList, TaskListSchema

@dataclass
class TaskListsResult:
    """ Result of calling the tasks API GET https://tasks.googleapis.com/tasks/v1/users/@me/lists endpoint """

    def __init__(self, etag, items, kind, next_page_token=None) -> None:
        self.etag = etag
        self.items = items
        self.kind = kind
        self.next_page_token = next_page_token

    etag: str
    items: list[TaskList]
    kind: str
    next_page_token: str


class TaskListsResultSchema(Schema):
    """ Schema for Marshmallow to serialize and deserialize TaskListsResult """
    model_class = TaskListsResult

    etag = fields.Str()
    items = fields.List(fields.Nested(TaskListSchema))
    kind = fields.Str()
    next_page_token = fields.Str()

    @post_load
    def make_task_lists_result(self, data, **kwargs) -> TaskListsResult:
        return type(self).model_class(**data)
