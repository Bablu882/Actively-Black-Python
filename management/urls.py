from django.urls import path,include 
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('',test1_view,name='test1'),
    path('add-user',add_user,name='add-user'),
    path('dashboard',dashboard,name='dashboard'),
    path('forgot-password',forgot_password,name='forgot-password'),
    path('listing',listing,name='listing'),
    path('login',login,name='login'),
    path('profile',profile,name='profile'),
    path('register',register,name='register'),
    path('logout',logout,name='logout'),
    path('verify-email/<slug:token>',verify_mail),
    path('forget-password',forget_password,name='forget-password'),
    path('change-password/<token>',change_password,name='change-password'),
    path('profile2/',profile2,name='profile2'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)