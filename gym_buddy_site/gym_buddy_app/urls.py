from django.conf.urls import url

from . import views

urlpatterns = [
    # ex:/gym_buddy/
    url(r'^$', views.index, name='index'),
    # ex:/gym_buddy/login/username/password
    url(r'^(?P<user_name>[\w]+)/(?P<user_password>[\w]+)/login/$', views.login, name='login'),
    # ex:/gym_buddy/register/username/password
    url(r'^(?P<user_name>[\w]+)/(?P<user_password>[\w]+)/register/$', views.register, name='register'),
]

