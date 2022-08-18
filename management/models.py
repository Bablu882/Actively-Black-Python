from email.policy import default
from operator import truediv
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    desc=models.TextField(max_length=500)        
    token=models.CharField(max_length=50)
    is_verified=models.BooleanField(default=False)
    avatar=models.ImageField(null=True,blank=True,default='default.png',upload_to='avatars')
    
class Forget_Password(models.Model):
    email=models.EmailField(max_length=50)
