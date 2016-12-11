from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

# user model
@python_2_unicode_compatible
class User(models.Model):
    user_name = models.CharField(max_length = 200)
    user_password = models.CharField(max_length = 200)
    def __str__(self):
        return self.user_name

# gym buddy request
@python_2_unicode_compatible
class Request(models.Model):
    request_time = models.DateTimeField('date published')
    # location, undecided
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.requester.user_name + ', time:' + self.request_time.strftime('%m/%d/%Y')

