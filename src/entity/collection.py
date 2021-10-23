from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar('T')

@dataclass
class Collection(Generic[T]):
	values: list[T]
	

	def filter(self, func) -> list[T]:
		return list(filter(func, self.values))