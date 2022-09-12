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


def account_activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save() 
        return render(request,'api/activate-success.html')  
    else: 
        return HttpResponse('Activation link is invalid!')                  


class LogoutUser(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,fromat=None):
        logout(request)
        return Response({'message':'User logout successfully'},status=status.HTTP_200_OK)

