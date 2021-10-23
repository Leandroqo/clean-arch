from abc import ABCMeta, abstractmethod
from src.entity.git import GitRepositories


class GitUseCaseInterface(metaclass=ABCMeta):
		@abstractmethod
		def list_user_repo(self, user: str) -> GitRepositories:
			raise NotImplementedError