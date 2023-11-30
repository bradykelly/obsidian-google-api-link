from dataclasses import dataclass
from marshmallow import Schema, fields


@dataclass
class TaskList:
    """ A TaskList from the Google Tasks API TaskListResult """
    etag: str
    id: str
    kind: str
    selfLink: str
    title: str
    updated: str

    def __repr__(self) -> str:
        return '<TaskList %r>' % self.title
    

class TaskListSchema(Schema):
    """ Schema for Marshmallow to serialize and deserialize TaskList """
    etag = fields.Str()
    id = fields.Str()
    kind = fields.Str()
    selfLink = fields.Str()
    title = fields.Str()
    updated = fields.Str()


