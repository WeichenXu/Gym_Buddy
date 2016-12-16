from django.conf.urls import url

from . import views

app_name = 'gym_buddy_app'
urlpatterns = [
    # index view, ex:/gym_buddy/
    url(r'^$', views.IndexView, name='index'),
    # request view, ex:/gym_buddy/request/user_id
    url(r'^(?P<user_id>[\w]+)/request/$', views.RequestView, name='request'),
    # ex:/gym_buddy/login, use POST
    url(r'^login/$', views.login, name='login'),
    # ex:/gym_buddy/register, use POST
    url(r'^register/$', views.register, name='register'),
    # ex:/gym_buddy/addRequest
    # parse the informaiton of the request througth POST
    url(r'^(?P<user_id>[\d]+)/addRequest/$', views.addRequest, name='addRequest'),
    # ex:/gym_buddy/confirmRequest
    # parse the reqeust id through POST
    url(r'^(?P<user_id>[\d]+)/(?P<from_request_id>[\d]+)/(?P<to_request_id>[\d]+)/confirmRequest/$', views.confirmRequest, name='confirmRequest'),
    # ex:/gym_buddy/requestDetail/
    # parse the request id
    url(r'^(?P<pk>[0-9]+)/requestDetail/$', views.requestView.as_view(), name='requestDetail'),
]

