
from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth import login as login_dj
from .decorator import authenticate_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail


def test1_view(request):
    return render(request,'management/test1.html')

def add_user(request):
    return render(request,'management/add-user.html')

def dashboard(request):
    return render(request ,'management/dashboard.html')    

def forgot_password(request):
    return render(request,'management/forget-password.html')    

def listing(request):
    return render(request,'management/listing.html')    

def profile(request):
    return render(request,'management/profile.html')



    
def register(request):
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Password should be at least 6 characters')
            context['has_error'] = True

        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Password mismatch')
            context['has_error'] = True

        if not username:
            messages.add_message(request, messages.ERROR,
                                 'Username is required')
            context['has_error'] = True

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR,
                                 'Username is taken, choose another one')
            context['has_error'] = True

            return render(request, 'management/register.html', context, status=409)

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Email is taken, choose another one')
            context['has_error'] = True

            return render(request, 'management/register.html', context, status=409)

        if context['has_error']:
            return render(request, 'management/register.html', context)

        uid=uuid.uuid4()
        user = User.objects.create(username=username, email=email)
        profile_obj=Profile.objects.create(user=user,token=uid)
        print(profile_obj)
        user.set_password(password)
        user.save()
        send_mail_after(user.email,uid)
        messages.add_message(request,messages.SUCCESS,'we have sent you a mail to verify your account')
        return redirect('register')

    return render(request, 'management/register.html')




@authenticate_user
def login(request):

    if request.method == 'POST':
        context = {'data': request.POST}
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        try:

            pro=Profile.objects.get(user=user)

            if not pro.is_verified:
                messages.add_message(request, messages.ERROR,
                                    'Email is not verified, please check your email inbox')
                return render(request, 'management/login.html', context, status=401)

            if user is not None:
                login_dj(request, user)
                messages.add_message(request, messages.SUCCESS,
                                f'Welcome {user.username}')
            else:

                messages.add_message(request, messages.ERROR,
                                    'Invalid credentials, try again')
                return render(request, 'management/login.html', context, status=401)
            return redirect('/dashboard')
        except Profile.DoesNotExist:
            messages.add_message(request,messages.ERROR,'Please provide valid credientials')
            return render(request,'management/login.html')

    return render(request, 'management/login.html')


def logout(request):

    auth_logout(request=request)

    messages.add_message(request, messages.SUCCESS,
                         'Successfully logged out')

    return redirect('/login')    



def send_mail_after(email,token):
    subject="verify email"
    message=f'click here http://127.0.0.1:8000/verify-email/{token}'
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)


def verify_mail(request,token):
    profile_id=Profile.objects.filter(token=token).first()
    print(profile_id)
    profile_id.is_verified=True
    profile_id.save()
    messages.success(request,'Your account is verified now you can login')
    return redirect('login')
