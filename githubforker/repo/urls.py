from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', login_required(views.RepoForkView.as_view()), name='repo_fork_url'),
    url(r'^fork/$', login_required(views.GithubForkView.as_view()), name='fork'),
]