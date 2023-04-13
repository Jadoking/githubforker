import requests
from django.conf import settings

def create_github_fork(fork_name: str):
    """Create a fork of the repo with the given name."""
    repo_owner = settings.REPO_OWNER
    repo_name = settings.REPO_NAME
    github_api_oauth_token = settings.GITHUB_API_OAUTH_TOKEN

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'token {github_api_oauth_token}'
    }

    request_body = {
        'name': fork_name
    }
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/forks'
    response = requests.post(url, headers=headers, json=request_body)

    return response