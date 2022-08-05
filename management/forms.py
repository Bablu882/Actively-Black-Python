
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models  import Profile

class RegisterForm(UserCreationForm):
    email=forms.EmailField()

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
            'minlength':'6'
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
            'minlength':'6'
        })

    class Meta:
        model=User
        fields=['username','email','password1','password2']



class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)

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
