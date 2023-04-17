# githubforker

This application will fork a github repo to an authorized Github account

This is done by making a call to the Github API using an Authorized OAuth token

For information on how to generate a token one can refer to this page (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-personal-access-token-classic) This token needs to have 'repos' permissions

This application uses Docker 4.18.0

After cloning please create an `.env` file in the project root with the following variables

```
DJANGO_SETTINGS_MODULE=config.settings
DJANGO_SECRET_KEY='[insert your django secret key]'
REPO_OWNER='[insert username of the github user the forked repo is in]'
REPO_NAME='[insert name of repo to be forked]'
GITHUB_API_OAUTH_TOKEN='[insert token here]'

```

Afterwards please run `docker compose up`

If you are running this for the first time it will build an image.

If in the future you need to rebuild the image you can run `docker compose build`
Sometimes certain actions during the build process get cached you can avoid this by running the above command with the arguement `--no-cache`

Once the docker container is up the API should be running on `localhost port 8000` (this can be changed in `docker-compose.yaml`)

The api endpoint to create a fork is as follows

```
localhost:8000/repo/fork/
```

This endpoint will fork the specified repo in the `.env` file to the Authenticated Github User that the Personal Access Token belongs to

In addition you it can accept query parameters to change certain settings related to the fork

- `fork_name` - The name of the fork to create.
- `default_branch_only` -  If True, the fork will only contain the default branch.

Example:
```
repo/fork/?fork_name=somenameforthefork?default_branch_only=False
```