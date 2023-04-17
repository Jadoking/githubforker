import pytest
from repo.utils import create_github_fork, process_fork_response
from repo.decorators import check_environment_variables_set
from unittest import mock
from django.conf import settings


@mock.patch('repo.utils.requests.post')
def test_create_github_fork_success(mock_post_request):
    # the personal token needs to have the repo scope and delete repo scope
    fork_args = {
        'fork_name': 'test_fork'
    }

    mock_post_request.return_value.status_code = 202
    mock_post_request.return_value.json.return_value = {
        'name': 'test_fork',
        'html_url':'testurl.com/test_fork'
    } 

    response = create_github_fork(**fork_args)
    assert response['message'] == 'Fork created successfully!'
    assert response['name'] == 'test_fork'
    assert response['html_url'] == 'testurl.com/test_fork'


@mock.patch('repo.utils.requests.post')
@pytest.mark.parametrize('status_code,message', 
                         [[400, 'Bad Request'], 
                          [403, 'Forbidden'], 
                          [404, 'Resource not found'], 
                          [422, 'Validation failed, or the endpoint has been spammed.']])
def test_create_github_fork_failure(mock_post_request, status_code, message):
    fork_args = {
        'fork_name': 'test_fork'
    }

    mock_post_request.return_value.status_code = status_code
    mock_post_request.return_value.json.return_value = {
        'message': message
    }

    response = create_github_fork(**fork_args)
    assert response['status_code'] == status_code
    assert response['message'] == message


def test_check_environment_variables_set():
    settings.REPO_OWNER = None
    @check_environment_variables_set
    def decorated():
        pass

    with pytest.raises(ValueError) as e:
        decorated()

    assert str(e.value) == 'Please set the REPO_OWNER, REPO_NAME, and GITHUB_API_OAUTH_TOKEN environment variables.' 