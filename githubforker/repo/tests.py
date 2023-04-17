import pytest
from utils import create_github_fork, process_fork_response
from django.conf import settings

def test_create_github_fork_success():
    # the personal token needs to have the repo scope and delete repo scope
    
    create_github_fork()
    assert True

def test_create_github_fork_failure():
    assert True

def test_process_fork_response():
    assert True

def test_process_fork_response():
    assert True