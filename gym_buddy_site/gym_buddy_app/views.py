from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Request

# Create your views here.
def index(request):
    return HttpResponse("Hello, app.")

# Login action
def login(request, user_name, user_password):
    response = "Login, user_name: %s, status: %s"
    try:
        login_user = User.objects.get(user_name = user_name)
        login_status = "Succeed" if login_user.user_password == user_password else "Invalid password" 
    except User.DoesNotExist:
        login_status = "Invalid user_name" 
    return HttpResponse(response % (user_name, login_status) )

# Register action
def register(request, user_name, user_password):
    response = "Register, user_name: %s, status: %s"
    try:
        user = User.objects.get(user_name = user_name)
        register_status = "Duplicated user_name"
    except User.DoesNotExist:
        user = User(user_name = user_name, user_password = user_password)
        user.save()
        register_status = "Succeed"
    return HttpResponse(response % (user_name,register_status) )
