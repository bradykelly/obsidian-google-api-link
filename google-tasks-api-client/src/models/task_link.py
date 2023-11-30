from dataclasses import dataclass
from marshmallow import Schema, fields


@dataclass
class TaskLink:
    """ Part of the Task model. A hyperlink to a related resource. """
    description: str
    link: str
    type: str

    def __repr__(self) -> str:
        return '<TaskLink %r>' % self.link    
    


class TaskLinkSchema(Schema):
    """ Schema for Marshmallow to serialize and deserialize TaskLink """
    description = fields.Str()
    link = fields.Str()
    type = fields.Str()