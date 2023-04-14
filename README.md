# githubforker

This application will fork a github repo to an authorized Github account

This is done by making a call to the Github API using an Authorized OAuth token

For information on how to generate a token one can refer to this page (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-personal-access-token-classic) This token needs to have 'repos' permissions

This token as well as a few other variables need to be set in a .env file at the root of the project

Currently due to the fact that we have not properly setup environment variable loading on virtualenv activation (WIP) you will need to 

run this command in terminal before running

```
export DJANGO_SETTINGS_MODULE=githubforker.settings
```

Until we setup a script to generate a .env file you will need these variables in your .env file

```

DJANGO_SECRET_KEY='[insert your django secret key]'
REPO_OWNER='[insert username of the github user the forked repo is in]'
REPO_NAME='[insert name of repo to be forked]'
GITHUB_API_OAUTH_TOKEN='[insert token here]'

```

Endpoint is coming but for the time being you can test the functionality in the python shell

```
from repo.utils import create_github_fork
create_github_fork('name-of-fork')
```

Still WIP so more will come