from src.adapter.git_adapter import GitAdapterInterface
from src.adapter.http_adapter import HttpAdapterInterface
from src.entity.git import GitRepositories, GitRepository


class Github(GitAdapterInterface):
	http_adapter: HttpAdapterInterface

	def __init__(self, http_adapter: HttpAdapterInterface) -> None:
		self.http_adapter = http_adapter


	def list_user_repo(self, user: str) -> GitRepositories:
			res = self.http_adapter._get('https://api.github.com/users/'+user+'/repos')
			return GitRepositories(values=[
				GitRepository(id=r['id'], name=r['name'])
				for r in res
			])