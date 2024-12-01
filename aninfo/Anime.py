from dataclasses import dataclass


@dataclass
class Anime:
    name: str
    name_cn: str
    date: str
    image: str
    summary: str
    tags: list[str]
    info: dict[str, str]
    eps: int
    id: int

    def __eq__(self, other):
        return self.id == other.id
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return hash(self.id)