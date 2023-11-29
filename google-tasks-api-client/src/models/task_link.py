from dataclasses import dataclass


@dataclass
class TaskLink:
    """ Part of the Task model """
    description: str
    link: str
    type: str

    def __repr__(self):
        return '<TaskLink %r>' % self.link    