import functools
from django.conf import settings

def check_environment_variables_set(func):
    """ Decorator that checks that the environment variables are set. """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        environment_variables_set = settings.REPO_OWNER and settings.REPO_NAME and settings.GITHUB_API_OAUTH_TOKEN
        if environment_variables_set:
            return func(*args, **kwargs)
        else:
            raise ValueError('Please set the REPO_OWNER, REPO_NAME, and GITHUB_API_OAUTH_TOKEN environment variables.')
    return wrapper