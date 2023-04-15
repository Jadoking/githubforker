import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from repo.utils import create_github_fork

class GithubForkView(View):

    def get(self, request):
        """Create a fork of the repo using the same name as the original github repo.
        It can also accept query parameters to customize the fork name and whether branches are forked as well.

        Query Parameters:
            fork_name (str): The name of the fork to create.
            default_branch_only (Bool): If True, the fork will only contain the default branch.
        
        Returns:
            response (Response): The response from the GitHub API.
        """
        query_params = request.GET
        fork_name = query_params.get('fork_name') or settings.REPO_NAME
        default_branch_only = query_params.get('default_branch_only')

        fork_args = {
            fork_name: fork_name
        }

        if default_branch_only:
            fork_args.update({
                'default_branch_only': default_branch_only
            })
        

        response = create_github_fork(**fork_args)
        return HttpResponse(json.dumps(response))
