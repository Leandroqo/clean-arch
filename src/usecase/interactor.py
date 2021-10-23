from src.adapter.git_adapter import GitAdapterInterface
from src.usecase.interface import GitUseCaseInterface
from src.entity.git import GitRepositories


class GitUsecase(GitUseCaseInterface):
	git_adapter: GitAdapterInterface


	def __init__(self, git_adapter: GitAdapterInterface) -> None:
		self.git_adapter = git_adapter

		
	def list_user_repo(self, user: str) -> GitRepositories:
		return self.git_adapter.list_user_repo(user)