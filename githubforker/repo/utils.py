import requests
from repo.decorators import check_environment_variables_set
from django.conf import settings

@check_environment_variables_set
def create_github_fork(fork_name: str, github_access_token: str, default_branch_only: bool = True) -> dict:
    """Create a fork of the repo with the given name.
    
    Args:
        fork_name (str): The name of the fork to create.
        default_branch_only (Bool): If True, the fork will only contain the default branch."
    
    Returns:
        response_json (Response): The response from the GitHub API.
    """
    repo_owner = settings.REPO_OWNER
    repo_name = settings.REPO_NAME
    
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'token {github_access_token}',
    }

    request_body = {
        'name': fork_name,
        'default_branch_only': default_branch_only,
    }

    # makes request to GitHub API
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/forks'
    response = requests.post(url, headers=headers, json=request_body)

    # parses response to JSON

    return process_fork_response(response)


def process_fork_response(response: requests.Response) -> dict:
    """Process the response from the GitHub API.
    
    Args:
        response (Response): The response from the GitHub API.
    
    Returns:
        response_json (dict): The response to be returned to the user.

    """
    response_content = response.json()

    response_json = {
        'status_code': response.status_code,
    }

    if response.status_code == 202:
        response_json.update({
            'message': 'Fork created successfully!',
            'name': response_content['name'],
            'html_url': response_content['html_url'],
        })
    elif "message" in response_content:
        response_json.update({
            'message': response_content['message'],
        })

    return response_json
