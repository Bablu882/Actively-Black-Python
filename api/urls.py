from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('api/register',RegisterUserAPI.as_view(),name='api/register'),
    path('api/login',LoginUser.as_view(),name='api/login'),
    path('api/logout',LogoutUser.as_view(),name='api/logout'),
    path('api/forget-password',ForgetPassword.as_view(),name='api/forget-password'),
    # path('account-activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',Account_activate.as_view(), name='account-activate'), 
    # path('account-activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',account_activate, name='account-activate'), 
    path('api/student',StudentView.as_view(),name='student'),
    path('api/student/<int:pk>/',StudentViewSet.as_view(),name='students'),
    path('api/mixin',StudentMixinList.as_view(),name='mixin'),
    path('api/mixin/<int:pk>/',StudentMixinDetail.as_view(),name='mixins'),
    path('api/generics',StudentGenericList.as_view(),name='generic'),
    path('api/generics/<int:pk>/',StudentGenericDetails.as_view(),name='generics')
    
 
    
]

