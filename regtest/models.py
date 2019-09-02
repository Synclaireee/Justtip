from django.db import models
from django.utils import timezone

# Create your models here.

class UserTest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, default='First_Name')
    last_name = models.CharField(max_length=255, default= 'Last_Name')
    description = models.CharField(max_length=255,blank=True)
    verification_status = models.CharField(max_length=255)
    profile_picture = models.TextField()
    
    def __str__(self):
        return self.id

    class Meta:
        ordering = ['created']