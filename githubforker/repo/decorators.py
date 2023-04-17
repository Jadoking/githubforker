import functools
from django.conf import settings


def check_environment_variables_set(func):
    """ Decorator that checks that the environment variables are set. """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        environment_variables_set = settings.REPO_OWNER and settings.REPO_NAME
        if environment_variables_set:
            return func(*args, **kwargs)
        else:
            raise ValueError('Please set the REPO_OWNER, and REPO_NAME environment variables.')
    return wrapper


def check_for_github_access_token(view_func):
    """ Decorator that checks that the user has a GitHub access token. """
    @functools.wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        if request.user.githubuserinfo.github_access_token:
            return view_func(self, request, *args, **kwargs)
        else:
            raise ValueError('Please set the github_access_token for the user.')
    return wrapper