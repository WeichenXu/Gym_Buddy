from django.conf.urls import url

from . import views

app_name = 'gym_buddy_app'
urlpatterns = [
    # ex:/gym_buddy/
    url(r'^$', views.index, name='index'),
    # ex:/gym_buddy/username/password/login
    url(r'^(?P<user_name>[\w]+)/(?P<user_password>[\w]+)/login/$', views.login, name='login'),
    # ex:/gym_buddy/username/password/register
    url(r'^(?P<user_name>[\w]+)/(?P<user_password>[\w]+)/register/$', views.register, name='register'),
    # ex:/gym_buddy/addRequest
    url(r'^(?P<user_id>[\d]+)/addRequest/$', views.addRequest, name='addRequest'),
    # ex:/gym_buddy/user_id/listRequest
    url(r'^(?P<user_id>[\d]+)/listRequest/$', views.listRequest, name='listRequest'),
]

