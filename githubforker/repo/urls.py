from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^fork/$', login_required(views.GithubForkView.as_view()), name='fork'),
]