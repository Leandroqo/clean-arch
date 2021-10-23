from src.infrastructure.github import Github
from src.infrastructure.httpx import HttpX
from src.usecase.interactor import GitUsecase


git = GitUsecase(Github(HttpX()))
resp = git.list_user_repo('leandroqo')
print(resp)
