
from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth import login as login_dj
from .decorator import authenticate_user
from django.contrib.auth.decorators import login_required
from .models import Profile
import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail


def test1_view(request):
    return render(request,'management/test1.html')
    
@login_required(login_url='login')
def add_user(request):
    return render(request,'management/add-user.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request ,'management/dashboard.html')    

def forgot_password(request):
    return render(request,'management/forget-password.html')    

@login_required(login_url='login')
def listing(request):
    return render(request,'management/listing.html')    

@login_required(login_url='login')
def profile(request):
    return render(request,'management/profile.html')



#Registration of new user    
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



#login user from here 
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

#Logout user from here
def logout(request):

    auth_logout(request=request)

    messages.add_message(request, messages.SUCCESS,
                         'Successfully logged out')

    return redirect('/login')    


#Send mail after registration
def send_mail_after(email,token):
    subject="verify email"
    message=f'click here http://127.0.0.1:8000/verify-email/{token}'
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)

#verify mail after registration send link to user mail 
def verify_mail(request,token):
    profile_id=Profile.objects.filter(token=token).first()
    print(profile_id)
    profile_id.is_verified=True
    profile_id.save()
    messages.success(request,'Your account is verified now you can login')
    return redirect('login')

##-----------------Forget password--------------------------------##

def forget_password(request):
    try:
        if request.method=='POST':
            user=request.POST.get('email')
            if not User.objects.filter(email=user).exists():
                messages.error(request,'Not user found with this email')
                return redirect('forget-password')
            else:    
                user_obj=User.objects.get(email=user)
                profile=Profile.objects.get(user=user_obj)
                pro=profile.token
                # token=str(uuid.uuid4())
                # profile_obj=Profile.objects.get(user=user_obj)
                # print(profile_obj)
                # print('profile_obj.token')
                # profile_obj.save()
                send_forget_password_mail(user,pro)
                messages.success(request,'please check your mail we have sent a link')
                return redirect('forget-password')
    except Exception as e:
        print(e)
    return render(request,'management/forget-password.html')

#Change forgot password 
def change_password(request,token):
    context={}
    try:
        profile=Profile.objects.filter(token=token).first()
        print(profile.user.id)
        if request.method == 'POST':
            newpass=request.POST.get('newpassword')
            conformpass=request.POST.get('conform-newpassword')
            user_id=request.POST.get('user_id')

            if user_id is None:
                messages.error(request,'No user is found')
                return redirect(f"/change-password/{token}/")

            if newpass != conformpass:
                messages.error(request,'password is missmatched')    
                return redirect(f"/change-password/{token}")

            user_obj=User.objects.get(id=user_id)    
            user_obj.set_password(newpass)
            user_obj.save()
            messages.success(request,'New password changed now login with new password')
            return redirect('login')
        context={'user_id':profile.user.id}  
    except Exception as e:
        print(e)
    return render(request,'management/change-password.html',context)    


#Send mail for forget password 
def send_forget_password_mail(email,token):
    subject="Change your password"
    message=f'click here http://127.0.0.1:8000/change-password/{token}'
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)


##----------------------------------------------------------------------------------------##

def profile2(request):
    return render(request,'management/profile2.html')