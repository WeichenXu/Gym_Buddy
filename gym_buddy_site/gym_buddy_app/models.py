from django.db import models

# Create your models here.

# user model
class User(models.Model):
    user_name = models.CharField(max_length = 200)
    user_password = models.CharField(max_length = 200)

# gym buddy request
class Request(models.Model):
    request_time = models.DateTimeField('date published')
    # location, undecided
    requester = models.ForeignKey(User, on_delete=models.CASCADE)


