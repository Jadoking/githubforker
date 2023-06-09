from django.db import models
from django.contrib.auth.models import User


class GithubUserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github_username = models.CharField(max_length=100)
    github_access_token = models.CharField(max_length=100)

    def __str__(self):
        return self.github_username
