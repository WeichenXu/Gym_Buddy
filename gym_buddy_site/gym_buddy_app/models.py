from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

# user model
@python_2_unicode_compatible
class User(models.Model):
    user_name = models.CharField(max_length = 200)
    user_password = models.CharField(max_length = 200)
    # gender choice
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    user_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    user_address = models.CharField(blank=True, max_length = 200)
    user_phone_number = models.CharField(blank=True, max_length = 200)
    def __str__(self):
        return self.user_name

# gym buddy request
@python_2_unicode_compatible
class Request(models.Model):
    request_time = models.DateTimeField('date published')
    # location
    longitude = models.DecimalField(default=0.0, max_digits=9, decimal_places=6)
    latitude = models.DecimalField(default=0.0, max_digits=9, decimal_places=6)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    # training part
    LEG = 'L'
    ARM = 'A'
    CHEST = 'C'
    TRAINING_CHOICES = (
        ('L', 'Leg'),
        ('A', 'Arm'),
        ('C', 'Chest'),
    )
    training_part = models.CharField(max_length=1, choices=TRAINING_CHOICES, default=LEG)
    training_weight = models.IntegerField(default=0)
    matched_request = models.ManyToManyField("self")
    recommend_request = models.ManyToManyField("self")
    def __str__(self):
        return self.requester.user_name + ', time:' + self.request_time.strftime('%m/%d/%Y')

