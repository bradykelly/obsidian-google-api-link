from dataclasses import dataclass


@dataclass
class TaskList:
    etag: str
    id: str
    kind: str
    selfLink: str
    title: str
    updated: str

    def __repr__(self):
        return '<TaskList %r>' % self.title