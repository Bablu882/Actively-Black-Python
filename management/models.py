from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from .managers import CustomUserManager
import uuid
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    desc=models.TextField(blank=True,null=True)        
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_verified=models.BooleanField(default=False)
    avatar=models.ImageField(null=True,blank=True,default='avatars/default.png',upload_to='avatars')
    address=models.CharField(max_length=500,blank=True,null=True)
    work_at=models.CharField(max_length=100,blank=True,null=True)
    display_name=models.CharField(max_length=50,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    post_code=models.CharField(max_length=50,blank=True,null=True)
    mobile_no=models.CharField(max_length=13,blank=True,null=True)
    country=models.CharField(max_length=50,blank=True,null=True)
    state=models.CharField(max_length=50,blank=True,null=True)
    customer='customer'
    vender='vender'
    account_select=[
        (customer,'customer'),
        (vender,'vender'),
    ]
    status=models.CharField(max_length=20,choices=account_select,default=customer,blank=True,null=True)
    admission=models.BooleanField(default=False,verbose_name=_("admission"),blank=True,null=True)
    referrals=models.IntegerField(default=0,blank=True,null=True)
    code=models.CharField(max_length=200,blank=True,null=True)
    recomended_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="recomended_by",blank=True,null=True)
    blance=models.FloatField(default=0.00,blank=True,null=True)
    requested=models.FloatField(default=0.00,blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_update=models.DateTimeField(auto_now=True,blank=True,null=True)
    slug=models.SlugField(blank=True,null=True,unique=True)
    facebook=models.URLField(blank=True,null=True)
    teitter=models.URLField(blank=True,null=True)
    instagram=models.URLField(blank=True,null=True)

    def __str__(self) -> str:
        return self.user.username

    def get_recomended_profile(self):
        queryset=Profile.objects.all()    
        my_records=[]
        for profile in queryset:
            if profile.recomended_by==self.user:
                my_records.append(profile)
        return my_records        

    def save(self,*args,**kwargs):
        self.slug=slugify(self.user.username)
        super().save(*args,**kwargs)
        # if not self.slug or self.slug is None or self.slug=="":
        #     self.slug=slugify(self.user.username,allow_unicode=True) 
        #     qs_exists=Profile.objects.filter(slug=self.slug).exists()   
        #     if qs_exists:
        #         self.slug=



    
class Forget_Password(models.Model):
    email=models.EmailField(max_length=50)

