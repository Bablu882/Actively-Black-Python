
from pickle import TRUE
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models  import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Div, Layout

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
            # 'required':'',
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
            # 'required':'',
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
            
            # 'email': None,
            # 'password   ':None,
            # 'password2':None

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
        def clean(self):
 
            # data from the form is fetched using super function
            super(LoginForm, self).clean()
            
            # extract the username and text field from the data
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
    
            # conditions to be met for the username length
            if len(username) < 5:
                self._errors['username'] = self.error_class([
                    'Minimum 5 characters required'])
            if len(password) <10:
                self._errors['text'] = self.error_class([
                    'Post Should Contain a minimum of 10 characters'])
    
            # return any errors if found
            return self.cleaned_data

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

class ChangePasswordForm(forms.Form):
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    conform_password=forms.CharField(max_length=50,widget=forms.PasswordInput)

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

from django.forms.utils import ErrorList

class DivErrorList(ErrorList):
     def __str__(self):
         return self.as_divs()

     def as_divs(self):
         if not self: return ''
         return '<div class="errorlist">%s</div>' % ''.join(['<div  class="errorlist">%s</div>' % e for e in self])
