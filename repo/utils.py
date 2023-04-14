import json
import requests
from django.conf import settings


def create_github_fork(fork_name: str, default_branch_only: bool = True):
    """Create a fork of the repo with the given name.
    
    Args:
        fork_name (str): The name of the fork to create.
        default_branch_only (Bool): If True, the fork will only contain the default branch."
    
    Returns:
        response (Response): The response from the GitHub API.
    """
    repo_owner = settings.REPO_OWNER
    repo_name = settings.REPO_NAME
    github_api_oauth_token = settings.GITHUB_API_OAUTH_TOKEN

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'token {github_api_oauth_token}',
    }

    request_body = {
        'name': fork_name,
        'default_branch_only': default_branch_only,
    }

    # makes request to GitHub API
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/forks'
    response = requests.post(url, headers=headers, json=request_body)

    # parses response to JSON
    response_json = json.loads(response.content)

    return process_fork_response(response_json)


def process_fork_response(response_json: dict):
    """Process the response from the GitHub API.
    
    Args:
        response_json (dict): The response from the GitHub API.
    
    Returns:
        response (dict): The response to be returned to the user.
    """
    if 'message' in response_json:
        response = {
            'status': 'error',
            'message': response_json['message'],
        }
    else:
        response = {
            'status': 'success',
            'message': 'Fork created successfully!',
            'name': response_json['name'],
            'html_url': response_json['html_url'],
        }

    return response