from dataclasses import dataclass
from marshmallow import Schema, fields
from task import Task, TaskSchema


@dataclass
class TasksResult:
    """ Result of calling the Tasks API https://tasks.googleapis.com/tasks/v1/lists/{tasklist}/tasks endpoint """
    etag: str
    items: list[Task]
    kind: str
    next_page_token: str



class TasksResultSchema(Schema):
    """ Schema for Marshmallow to serialize and deserialize TasksResult """
    etag = fields.Str()
    items = fields.List(fields.Nested(TaskSchema))
    kind = fields.Str()
    next_page_token = fields.Str()
