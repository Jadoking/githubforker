# Github Forker

This application will fork a github repo to an authorized Github account

This is done by making a call to the Github API using an Personal Acccess Token (legacy)

For information on how to generate a token one can refer to this page (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-personal-access-token-classic) This token needs to have 'repos' permissions

## Requirements
- Python 3.7.16
- Docker 4.18.0

## Installation

This application uses Docker 4.18.0

1. Clone Repo
2. After Cloning the repo please create a `.env` file in the project root with the following environment variables. Anything in brackets like these [] can be replaced to your liking
```
ENVIRONMENT=dev

DJANGO_SETTINGS_MODULE=config.settings

DJANGO_SECRET_KEY=[your_secret]
REPO_OWNER=[your_github]
REPO_NAME=[your_repo]

MYSQL_ROOT_PASSWORD=[your_root_password]

MYSQL_DATABASE=[your_database]
MYSQL_USER=[your_admin]
MYSQL_PASSWORD=[your_password]
MYSQL_DATABASE_HOST=mysql-db
MYSQL_DATABASE_PORT=3306

```
3. run `docker compose up` this should build the containers if it's the first time running.
4. run `docker compose exec app python githubforker/manage.py migrate` to run database migrations

## Useful Information

Upon running docker compose up the server should be running at port 8000. If for some reason it isn't up you can run the following command `docker compose exec app python githubforker/manage.py runserver 0.0.0.0:8000`

If in the future you need to rebuild the image you can run `docker compose build`
Sometimes certain actions during the build process get cached you can avoid this by running the above command with the arguement `--no-cache`

Once the docker container is up the API should be running on `localhost port 8000` (this can be changed in `docker-compose.yaml`)

## Usage

1. run `docker compose exec app python githubforker/manage.py createsuperuser` to create a user
2. login at `localhost:8000/admin`
3. After a user is created and logged in you can add a `Github User Info` object you can do this at `localhost:8000/admin/repo/githubuserinfo`
4. once that is setup you can use the endpoint for the authenticated user


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