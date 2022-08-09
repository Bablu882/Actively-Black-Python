from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)        
    token=models.CharField(max_length=50)
    is_verified=models.BooleanField(default=False)
    
class Forget_Password(models.Model):
    email=models.EmailField(max_length=50)
