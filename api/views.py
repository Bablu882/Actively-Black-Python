from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import redirect,render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.conf import settings
from django.core.mail import send_mail
from management.views import send_forget_password_mail
from management.token import account_activation_token

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterUserAPI(APIView):
    def post(self,request,format=None):
        serializer=RegisterSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({'message':'Email has been sent please check your mail and verify','token':token},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class LoginUser(APIView):
    def post(self,request,format=None):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username=serializer.data.get('username')
            password=serializer.data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
               token=get_tokens_for_user(user)
               return Response({'message':'login success','token':token})
            else:
                return Response({'error':{'non_field_errors':['invalid credentials']}},status=status.HTTP_404_NOT_FOUND)


class LogoutUser(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,fromat=None):
        logout(request)
        return Response({'message':'User logout successfully'},status=status.HTTP_200_OK)


class ForgetPassword(APIView):
    def post(self,request,format=None):
        data=request.data
        email=data['email']
        user=User.objects.get(email=email)
        user.is_active=False
        user.save()
        current_site=get_current_site(request)
        mail_subject="password reset request"
        message = render_to_string('api/activate.html', {  
                    'user': user,  
                    'domain': current_site.domain,  
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                    'token':account_activation_token.make_token(user),  
                })
        to_email = email  
        email = EmailMessage(  
                    mail_subject, message, to=[to_email]  
        )  
        email.send()
        return Response({'message':'Forget password email has been sent please check your inbox'})
        



# def register(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         try: 
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 user=form.save(commit=False)
#                 user.is_active=False
#                 user.save()
#                 current_site=get_current_site(request)
#                 mail_subject='verify mail'
#                 message = render_to_string('management/activate.html', {  
#                     'user': user,  
#                     'domain': current_site.domain,  
#                     'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
#                     'token':account_activation_token.make_token(user),  
#                 })
#                 to_email = form.cleaned_data.get('email')  
#                 email = EmailMessage(  
#                             mail_subject, message, to=[to_email]  
#                 )  
#                 email.send()
#                 token=uuid.uuid4()
#                 print(token)
#                 Profile.objects.create(user=user,token=token) 
#                 messages.add_message(request,messages.SUCCESS,'we have sent you a mail to verify your account')
#         except Exception as e:
#             logging.error(e)
#             return redirect('/register')
#     else:
#         form = RegisterForm()
#     return render(request, 'management/register.html', {'form':form}) 



# def send_forget_password_mail(email,token):
#     subject="Change your password"
#     message=f'click here http://127.0.0.1:8000/change-password/{token}'
#     from_email=settings.EMAIL_HOST_USER
#     recipient_list=[email]
#     send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)





# class Account_activate(APIView):
#     def post(self,request,uidb64,token,format=None):
#         User = get_user_model()
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid) 
#         if user is not None and account_activation_token.check_token(user, token): 
#             user.is_active=True
#             user.save()
#             return Response({'message':'account activation successful now you can login'})
#         else:
#             return Response({'error':'invalid link !'}) 


# def account_activate(request, uidb64, token):  
#     User = get_user_model()  
#     try:  
#         uid = force_str(urlsafe_base64_decode(uidb64))  
#         user = User.objects.get(pk=uid)  
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
#         user = None  
#     if user is not None and account_activation_token.check_token(user, token):  
#         user.is_active = True  
#         user.save() 
#         return render(request,'api/activate-success.html')  
#     else: 
#         return HttpResponse('Activation link is invalid!')                  



# def send_forget_password_mail(email,token):
#     subject="Change your password"
#     message=f'click here http://127.0.0.1:8000/change-new-password/{token}'
#     from_email=settings.EMAIL_HOST_USER
#     recipient_list=[email]
#     send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)

# class ForgetPassword(APIView):
#     def post(self,request,format=None):
#         data=request.data
#         email=data['email']
#         user=User.objects.get(email=email)
#         profile=Profile.objects.get(user=user)
#         token=profile.token
#         if User.objects.filter(email=email).exists():
#             send_forget_password_mail(email,token)
#             return Response({'message':'Forget password email has been sent please check your inbox'})
        
#         return Response({'error':'Email Doesnot exists'},status=status.HTTP_400_BAD_REQUEST)    




