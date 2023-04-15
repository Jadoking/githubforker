from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^fork/$', views.GithubForkView.as_view(), name='fork'),
]