from django.urls import path,include 
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views #import this



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
    # path('verify-email/<slug:token>',verify_mail),
    path('forget-password',forget_password,name='forget-password'),
    path('change-password/<token>',change_password,name='change-password'),
    path('profile2/',profile2,name='profile2'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',activate, name='activate'), 
    # path('change-password/<uidb64>/<token>/',change_password, name='change-password'),
    # path('change-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="management/change-password.html"), name='password_reset_confirm'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)