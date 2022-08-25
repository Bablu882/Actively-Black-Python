
from types import CodeType
from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth import login as login_dj
from .decorator import authenticate_user
from django.contrib.auth.decorators import login_required
from .models import Profile,User
import uuid
from django.core.mail import send_mail,BadHeaderError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.http import HttpResponse  
from django.utils.encoding import force_bytes  
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from .token import account_activation_token
from .forms import ChangePasswordForm, ForgetPasswordform, RegisterForm,LoginForm, Userchangeform,ProfileForm
from django.db.models import Q





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
    users=User.objects.all()
    return render(request,'management/listing.html',{'user':users})

@login_required(login_url='login')
def profile(request):
    return render(request,'management/profile.html')


###------------------------------------Register User------------------------------------###

@authenticate_user
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            current_site=get_current_site(request)
            mail_subject='verify mail'
            message = render_to_string('management/activate.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()
            token=uuid.uuid4()
            print(token)
            profile=Profile.objects.create(user=user,token=token) 
            print(profile)
            messages.add_message(request,messages.SUCCESS,'we have sent you a mail to verify your account')

            return redirect('register')

    else:
        form = RegisterForm()
    return render(request, 'management/register.html', {'form':form}) 

###-------------------------------------Click For Activate----------------------------------###

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect('login')  
    else:  
        return HttpResponse('Activation link is invalid!')       


##--------------------------------LOGOUT---------------------------------------##

def logout(request):

    auth_logout(request=request)

    messages.add_message(request, messages.SUCCESS,
                         'Successfully logged out')

    return redirect('/login')    




##-----------------Forget password--------------------------------##

def forget_password(request):
    form=ForgetPasswordform()
    try:
        if request.method=='POST':
            form=ForgetPasswordform(request.POST)
            if form.is_valid(): 
                user=form.cleaned_data['email']
                if not user:
                    message="Please provide your valid email"
                    return render(request,'management/forget-password.html',context={'message':message})
                if not User.objects.filter(email=user).exists():
                    messages.error(request,'Not user found with this email')
                    return redirect('forget-password')
                else:    
                    user_obj=User.objects.get(email=user)
                    profile=Profile.objects.get(user=user_obj)
                    pro=profile.token
                    print(pro)
                    send_forget_password_mail(user,pro)
                    messages.success(request,'please check your mail we have sent a link')
                    return redirect('forget-password')
    except Exception as e:
        print(e)
    return render(request,'management/forget-password.html',{'form':form})

###-----------------------------Redirect On Change Password Form---------------------------##

def change_password(request,token):
    form=ChangePasswordForm()
    profile=Profile.objects.filter(token=token).first()
    print(profile.user.id)
    if request.method=='POST':
        user_id=request.POST.get('user_id')
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            newpass=form.cleaned_data['password']
            user_obj=User.objects.get(id=user_id)
            user_obj.set_password(newpass)
            user_obj.save()
            messages.success(request,'New password changed now login with new password')
            return redirect('login')
    return render(request,'management/change-password.html',{'form':form,'user_id':profile.user.id})

###------------------------------------Forget Password Mail---------------------------------###

def send_forget_password_mail(email,token):
    subject="Change your password"
    message=f'click here http://127.0.0.1:8000/change-password/{token}'
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)


##----------------------------------------LOGIN------------------------------------------------##

def login(request):
    form =LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user and not user.is_active:
                messages.error(request,'please verify email ')
                return redirect('login')
            if user is not None:
                login_dj(request, user)
                messages.success(request,f'Welcome {user.username}')
                return redirect('dashboard')
            else:
                messages.error(request,'Provide valid credentials or check your mail')
    return render(
        request, 'management/login.html', context={'form': form, 'message': message}) 

###------------------------------------Admin Add User------------------------------------------------####

@login_required(login_url='login')
def add_user_admin(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            token=uuid.uuid4()
            Profile.objects.create(user=user,token=token)
            form=RegisterForm()
            messages.success(request,'Add user successfully')
    else:
        form=RegisterForm()        
    return render(request,'management/admin-add-user.html',{'form':form})

###------------------------------------Admin Delete User------------------------------------###

@login_required(login_url='login')
def delete_user(request,id):
        user=User.objects.get(pk=id)
        user.delete()
        messages.success(request,'User deleted successfully !!')
        return redirect('listing')

###-----------------------------------Admin Edit User--------------------------------------###

@login_required(login_url='login')
def edit_user(request,id):
    request.method=='POST'
    gt=User.objects.get(pk=id)
    pro=Profile.objects.get(pk=id)
    form=Userchangeform(request.POST,request.FILES,instance=gt)
    form2=ProfileForm(request.POST,request.FILES,instance=pro)
    if form.is_valid() and form2.is_valid():
        form.save()
        form2.save()
        messages.success(request,'User updated successfully!!')

    else:
        gt=User.objects.get(pk=id)
        pro=Profile.objects.get(pk=id)
        form=Userchangeform(instance=gt)
        form2=ProfileForm(instance=pro)
    return render(request,'management/change-user-form.html',{'form':form,'form2':form2,'image':gt})

###---------------------------------------Edit User Profile---------------------------------###

@login_required(login_url='login')
def edit_profile(request):
    request.method=='POST'
    gt=User.objects.get(id=request.user.id)
    form=Userchangeform(request.POST,instance=gt)
    form2=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
    if form.is_valid() and form2.is_valid():
        form.save()
        form2.save()
        messages.success(request,'Profile updated successfully!!')
        return redirect('profile')

    else:
        gt=User.objects.get(id=request.user.id)
        form=Userchangeform(instance=gt)
        form2=ProfileForm(instance=request.user.profile)
    return render(request,'management/edit-profile.html',{'form':form,'form2':form2})    


@login_required(login_url='login')
def view_user_profile(request,id):
    gt=User.objects.get(pk=id)
    pro=Profile.objects.get(pk=id)
    form=Userchangeform(instance=gt)
    form2=ProfileForm(instance=pro)
    image=pro.avatar
    return render(request,'management/view-profile.html',{'form':form,'form2':form2,'image':image})    

###---------------------------------------------------------------------------------------###
