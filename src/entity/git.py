from dataclasses import dataclass
from src.entity.collection import Collection

@dataclass
class GitRepository:
	id: int
	name: str


@dataclass
class GitRepositories(Collection[GitRepository]):
	values: list[GitRepository]