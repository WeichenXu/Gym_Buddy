from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.template import loader
from django.urls import reverse

from .models import User, Request

# Create your views here.
def IndexView(request):
    template = loader.get_template('gym_buddy_app/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

# List all request of a user
def RequestView(request, user_id):
    user = User.objects.get(id = user_id)
    request_list = Request.objects.filter(requester = user)
    template = loader.get_template('gym_buddy_app/list_request.html')
    context = {
        'user_name': user.user_name,
        'request_list': request_list
    }
    return HttpResponse(template.render(context, request))

# Login action
# {'user_name':xxx, 'user_password':xxx}
def login(request):
    # parse the parameters
    try:
        user_name = request.POST['user_name']
        print (user_name)
        user_password = request.POST['user_password']
        print (user_password)
    except KeyError:
        return render(request, 'gym_buddy_app/index.html', {
            'error_message':"Please parse user_name & user_password.",
        })
    try:
        login_user = User.objects.get(user_name = user_name)
        if login_user.user_password != user_password: 
            return render(request, 'gym_buddy_app/index.html', {
                'error_message':"Invalid password",
            })
    except User.DoesNotExist:
        return render(request, 'gym_buddy_app/index.html', {
            'error_message':"Invalid user_name",
        })
    return HttpResponseRedirect(reverse('gym_buddy_app:request', args=(login_user.id,)))

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

# Add a request of a user
def addRequest(request, user_id):
    user = User.objects.get(id = user_id)
    req = Request(request_time = timezone.now(), requester = user)
    req.save()

