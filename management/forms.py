
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.contrib.auth import authenticate

##------------------------------REGISTRATION FORM------------------------------##

class RegisterForm(UserCreationForm):
    username=forms.CharField(error_messages={'required':'enter your username'})
    email=forms.EmailField(error_messages={'required':'enter your email'})
    password1 = forms.CharField(error_messages={'required':'enter your password'},widget=forms.PasswordInput)
    password2 = forms.CharField(error_messages={'required':'enter your conform password'},widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.fields["username"].widget.attrs.update({
            # 'required':'',
            'name':'username',
            'id':'username',
             'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'Username',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["email"].widget.attrs.update({
            # 'required':'',
            'name':'email',
             'style':'height:40px',
            'size':'50px',
            'id':'email',
            'type':'text',
            'class':'form-control',
            'placeholder':'Email',
            'maxlength':'50',
            'minlength':'6',
        })
        self.fields["password1"].widget.attrs.update({
            'name':'password1',
            'size':'50px',
            'style':'height:40px',
            'id':'password1',
            'type':'text',
            'class':'form-control',
            'placeholder':'password',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["password2"].widget.attrs.update({
            'name':'password2',
            'id':'password2',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'color':'red',
            'class':'form-control',
            'placeholder':'Conform password',
            'maxlength':'50',
            'minlength':'6',
        })

    class Meta:
        model=User
        fields=['username','email','password1','password2']
    
        help_texts = {
            'username': None,
        }

    def clean_username(self):
        username=self.cleaned_data['username']    
        if len(username) <=3:
            raise forms.ValidationError('username is to short ')
        return username 

    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email is already taken')       
        return email    

##----------------------------LOGIN FORM ----------------------------------##

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,error_messages={'required':'enter your username'})
    password=forms.CharField(max_length=50,widget=forms.PasswordInput,error_messages={'required':'enter your password'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            # 'required':'',
            'name':'username',
            'id':'username',
             'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            # 'placeholder':'Username',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["password"].widget.attrs.update({
            # 'required':'',
            'name':'password',
             'style':'height:40px',
            'size':'50px',
            'id':'password',
            'type':'text',
            'class':'form-control',
            # 'placeholder':'password',
            'maxlength':'50',
            'minlength':'6'
        })
    def clean_username(self):
        username=self.cleaned_data['username']    
        if not  User.objects.filter(username=username).exists():
            raise forms.ValidationError('username doesnot exist ')
        return username

    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     if password:
    #         self.password = authenticate(password=password)
    #         if self.password is None:
    #             raise forms.ValidationError("Please enter a correct password!")
    #         elif not self.password.is_active:
    #             raise forms.ValidationError("This account is inactive.") 

    #     return password
            
##-----------------------FORGET PASSWORD FORM-------------------------------##
class ForgetPasswordform(forms.Form):
    email=forms.EmailField() 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            # 'required':'',
            'name':'email',
            'id':'email',
             'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            # 'placeholder':'Username',
            'maxlength':'50',
            'minlength':'6'
        })
    def clean_email(self):
        email=self.cleaned_data['email']    
        if not  User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email doesn't exist")
        return email      

class ChangePasswordForm(forms.Form):
    password=forms.CharField(error_messages={'required':'enter new-password'},widget=forms.PasswordInput,validators=[validate_password])
    conform_password=forms.CharField(error_messages={'required':'enter conform new-password'},widget=forms.PasswordInput,validators=[validate_password])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget.attrs.update({
            # 'required':'',
            'name':'password',
            'id':'password',
             'style':'height:40px',
            'size':'50px',
            'type':'text',
            'placeholder':'password',
            'class':'form-control',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["conform_password"].widget.attrs.update({
            'name':'conform_password',
             'style':'height:40px',
            'size':'50px',
            'id':'conform_password',
            'type':'text',
            'class':'form-control',
            'placeholder':'conform-password',
            'maxlength':'50',
            'minlength':'6'
        })
    def clean_conform_password(self):
        password = self.cleaned_data['password']
        conform_password = self.cleaned_data['conform_password']
        if password and conform_password:
                if password != conform_password:
                   raise forms.ValidationError('Password mismatch')
        return conform_password
