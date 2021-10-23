from src.adapter.git_adapter import GitAdapterInterface
from src.entity.git import GitRepositories, GitRepository


class Bitbucket(GitAdapterInterface):
	def list_user_repo(self, user: str) -> GitRepositories:
			return GitRepositories(values=[
				GitRepository(id=1, name=user)
			])
