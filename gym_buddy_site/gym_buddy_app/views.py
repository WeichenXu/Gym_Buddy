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
    # update recommendation for user request
    for req in request_list:
        recommend(req.id)
    template = loader.get_template('gym_buddy_app/list_request.html')
    context = {
        'user': user,
        'request_list': request_list,
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
# {'user_name':xxx, 'user_password':xxx}
def register(request):
    # parse the parameters
    try:
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
    except KeyError:
        return render(request, 'gym_buddy_app/index.html', {
            'error_message':"Please parse user_name & user_password.",
        })
    try:
        user = User.objects.get(user_name = user_name)
        return render(request, 'gym_buddy_app/index.html', {
            'error_message':"Please choose another username, previous one has already been used by others",
        })
    except User.DoesNotExist:
        user = User(user_name = user_name, user_password = user_password)
        user.save()
        register_status = "Succeed"
        return HttpResponseRedirect(reverse('gym_buddy_app:request', args=(user.id,)))

# Add a request of a user
# POST {'time':xx-xx:xx, 'longitude':xx.xx, 'latitude':xx.xx, 'training_part':Leg, 'training_weight':xx}
def addRequest(request, user_id):
    # parse the parameters
    try:
        time_get = request.POST['time']
        longitude_get = request.POST['longitude']
        latitude_get = request.POST['latitude']
        training_part_get = request.POST['training_part']
        training_weight_get = request.POST['training_weight']
    except KeyError:
        print ('Please parse the parameters')
        return HttpResponseRedirect(reverse('gym_buddy_app:request', args=(user.id,)))
    user = User.objects.get(id = user_id)
    req = Request(request_time = time_get, longitude = longitude_get, latitude = latitude_get, requester = user )
    req.save()
    return HttpResponseRedirect(reverse('gym_buddy_app:request', args=(user.id,)))

# Confirm a request
# from_request_id: the request id who confirm, to...: request be confirmed
# POST {'request_id':xxxx}
def confirmRequest(request, user_id, from_request_id, to_request_id):
    from_req = Request.objects.get(id = from_request_id)
    to_req = Request.objects.get(id = to_request_id)
    from_req.matched_request.add(to_req)
    to_req.save()
    return HttpResponseRedirect(reverse('gym_buddy_app:request', args=(user_id,)))

# Recommend function for the request
# Iterate all requests in the database and add recommended ones
def recommend(request_id):
    req = Request.objects.get(id = request_id)
    recommend_req = Request.objects.all().exclude(requester=req.requester)
    for rec in recommend_req:
        req.recommend_request.add(rec)
    req.save()
