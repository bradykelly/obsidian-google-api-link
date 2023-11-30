from dataclasses import dataclass
from datetime import datetime
from marshmallow import Schema, fields
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

    def __repr__(self) -> str:
        return '<Task %r>' % self.title
    

class TaskSchema(Schema):
    """ Schema for Marshmallow to serialize and deserialize Task """
    kind = fields.Str()
    id = fields.Str()
    title = fields.Str()
    status = fields.Str()
    notes = fields.Str()
    parent = fields.Str()
    position = fields.Int()
    completed = fields.Str()
    deleted = fields.Bool()
    due = fields.DateTime()
    etag = fields.Str()
    hidden = fields.Bool()
    selfLink = fields.Str()
    updated = fields.DateTime()
    links = fields.List(fields.Nested(TaskLink))