
from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth import login as login_dj
from .decorator import authenticate_user
from django.contrib.auth.decorators import login_required
from .models import Profile
import uuid
from django.contrib.auth.models import User
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
from .forms import ForgetPasswordform, RegisterForm




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



#login user from here 


def logout(request):

    auth_logout(request=request)

    messages.add_message(request, messages.SUCCESS,
                         'Successfully logged out')

    return redirect('/login')    




##-----------------Forget password--------------------------------##

def forget_password(request):
    try:
        if request.method=='POST':
            user=request.POST.get('email')
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

            if len(newpass) < 6:
                messages.error(request,'password required atleast 6 charactor')
                return redirect(f"/change-password/{token}")

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




from django.contrib.auth import login, authenticate 
from .forms import LoginForm # add to imports

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
                return redirect('dashboard')
            else:
                messages.error(request,'Provide valid credentials or check your mail')
    return render(
        request, 'management/login.html', context={'form': form, 'message': message}) 

# from .forms import ForgetPasswordform
# # def forget_password(request):
# #     form=ForgetPasswordform()
# #     if request.method=='POST':
# #         form=ForgetPasswordform(request.POST)        
# #         if form.is_valid():
# #             user=form.cleaned_data['email']
# #             username=User.objects.filter(email=user)
# #             current_site=get_current_site(request)
# #             mail_subject='verify mail'
# #             message = render_to_string('management/activate-forget-password.html', {  
# #                 'user': username,  
# #                 'domain': current_site.domain,  
# #                 'uid':urlsafe_base64_encode(force_bytes(username.pk)),  
# #                 'token':account_activation_token.make_token(username),  
# #             })
# #             to_email = form.cleaned_data.get('email')  
# #             email = EmailMessage(  
# #                         mail_subject, message, to=[to_email]  
# #             )  
# #             email.send() 
# #             messages.add_message(request,messages.SUCCESS,'we have sent you a mail to verify your account')
# #         else:
# #             messages.error(request,'invilid email')
# #             return render(request,'management/activate-forget-password.html')
            
# #     else:
# #         form=ForgetPasswordform()    
# #             # clean=form.cleaned_data['email']
# #     return render(request,'management/forget-password.html',{'form':form})


# from django.db.models.query_utils import Q


# # def forget_password(request):

# # 	if request.method == "POST":
# # 		password_reset_form = ForgetPasswordform(request.POST)
# # 		if password_reset_form.is_valid():
# # 			data = password_reset_form.cleaned_data['email']
# # 			associated_users = User.objects.filter(Q(email=data))
# # 			if associated_users.exists():
# # 				for user in associated_users:
# # 					subject = "Password Reset Requested"
                    
# # 					email_template_name = "management/activate-forget-password.html"
# # 					c = {
# # 					"email":user.email,
# # 					'domain':'127.0.0.1:8000',
# # 					'site_name': 'Website',
# # 					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
# # 					"user": user,
# # 					'token': account_activation_token .make_token(user),
# # 					'protocol': 'http',
        
# # 					}
# # 					email = render_to_string(email_template_name, c)
                
# # 					try:
# # 						send_mail(subject, email, recipient_list=[data], fail_silently=False,from_email=settings.EMAIL_HOST_USER)
# # 					except BadHeaderError:
# # 						return HttpResponse('Invalid header found.')
# # 					return redirect ("forget-password")
# # 	password_reset_form = ForgetPasswordform()
# # 	return render(request, "management/forget-password.html", context={"password_reset_form":password_reset_form})


#     # current_site=get_current_site(request)
#     #         mail_subject='verify mail'
#     #         message = render_to_string('management/activate.html', {  
#     #             'user': user,  
#     #             'domain': current_site.domain,  
#     #             'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
#     #             'token':account_activation_token.make_token(user),  
#     #         })
#     #         to_email = form.cleaned_data.get('email')  
#     #         email = EmailMessage(  
#     #                     mail_subject, message, to=[to_email]  
#     #         )  
#     #         email.send() 
# from .forms import ChangePasswordForm
# # def activate_forget_email(request,token):
# #     form=ChangePasswordForm()
# #     if request.method=='POST':
# #         form=ChangePasswordForm(request.POST)
# #         password=form.cleaned_data[password]
# #         conform_password=form.cleaned_data[conform_password]
# #         if password!=conform_password:
# #             messages.error(request,'both password must be same')
# #             return redirect('forget-password/{token}')
# #     return render(request,'management/change-password.html',{'form':form})


# # from django.contrib.auth import update_session_auth_hash

# # def change_password(request,token):
# #     form=ChangePasswordForm()
# #     # if request.method == 'POST':
# #     #     form = ChangePasswordForm(user=request.user, data=request.POST)
# #     #     if form.is_valid():
# #     #         pass
# #     #         update_session_auth_hash(request, form.user)
# #     #         return redirect('dashboard')
# #     # else:

    
# #     return render(request,'management/change-password.html',{'form':form})

# # def change_password(request, uidb64, token):  
# #     User = get_user_model()  
# #     try:  
# #         uid = force_str(urlsafe_base64_decode(uidb64))  
# #         user = User.objects.get(pk=uid)  
# #     except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
# #         user = None  
# #     if user is not None and account_activation_token.check_token(user, token):  
# #         user.is_active = True  
# #         user.save()  
# #         return redirect('login')  
# #     else:  
# #         return HttpResponse('Activation link is invalid!') 





