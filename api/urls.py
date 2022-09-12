from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('register',RegisterUserAPI.as_view(),name='register'),
    path('login',LoginUser.as_view(),name='login'),
    # path('account-activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',Account_activate.as_view(), name='account-activate'), 
    path('account-activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',account_activate, name='account-activate'), 
    # path('logout',LogoutUser.as_view(),name='logout'),
 
    
]

