
from dataclasses import field
from pyexpat import model
from urllib import request
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages



##------------------------------REGISTRATION FORM------------------------------##

class RegisterForm(UserCreationForm):
    username=forms.CharField(error_messages={'required':'Enter your username'})
    email=forms.EmailField(error_messages={'required':'Enter your email'})
    password1 = forms.CharField(error_messages={'required':'Enter your password'},widget=forms.PasswordInput)
    password2 = forms.CharField(error_messages={'required':'Enter your confirm password'},widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.fields["username"].widget.attrs.update({
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
            'placeholder':'Password',
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
            'placeholder':'Confirm password',
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
            raise forms.ValidationError('username is too short ')
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


class Userchangeform(UserChangeForm):
    # first_name=forms.CharField(max_length=50,error_messages={'required':'Enter username'})
    # last_name=forms.CharField(max_length=50,error_messages={'required':'Enter last name'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.fields["username"].widget.attrs.update({
            
            'name':'username',
            'id':'username',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'Username',
            'maxlength':'50',
            'minlength':'6',
            'value':''
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
        self.fields["first_name"].widget.attrs.update({
            'name':'first_name',
            'size':'50px',
            'style':'height:40px',
            'id':'first_name',
            'type':'text',
            'class':'form-control',
            'placeholder':'first_name',
            'maxlength':'50',
            'minlength':'6'
        })
        self.fields["last_name"].widget.attrs.update({
            'name':'last_name',
            'id':'last_name',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'color':'red',
            'class':'form-control',
            'placeholder':'last_name',
            'maxlength':'50',
            'minlength':'6',
        })
        self.fields["user_permissions"].widget.attrs.update({
            'name':'user_permissions',
            'id':'user_permissions',
            'style':'height:200px',
            'size':'50px',
            'type':'text',
            'color':'red',
            'class':'form-control',
            'placeholder':'user_permissions',
            'maxlength':'50',
            'minlength':'6',
        })
        self.fields["date_joined"].widget.attrs.update({
            'name':'date_joined',
            'id':'date_joined',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'color':'red',
            'class':'form-control',
            'placeholder':'date_joined',
            'maxlength':'50',
            'minlength':'6',
        })
        self.fields["last_login"].widget.attrs.update({
            'name':'last_login',
            'id':'last_login',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'color':'red',
            'class':'form-control',
            'placeholder':'last_login',
            'maxlength':'50',
            'minlength':'6',
        })
    # def clean(self):
    #     email=self.cleaned_data['email']    
        
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('Email already exist !')
    #         # messages.success(request,'email already exist')



    class Meta:
        model=User
        fields=['username','first_name','last_name','email','is_superuser','is_staff','is_active','last_login','date_joined','user_permissions']




from django.contrib.auth.models import Permission

class Permissionform(forms.ModelForm):
    class Meta:
        model=Permission
        fields='__all__'   

from .models import Profile

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.fields["avatar"].widget.attrs.update({
            
            'name':'avatar',
            'id':'avatar',
            'style':'height:40px',
            'size':'50px',
            'type':'text',
            'class':'form-control',
            'placeholder':'avatar',
            'maxlength':'50',
            'minlength':'6',
            'value':''
        })

    class Meta:
        model=Profile
        fields=['avatar']
###---------------------------------------------------------------------------------------####        
class PermissionsModelMultipleChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name



from django.contrib.auth.models import PermissionsMixin,PermissionManager
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission,PermissionManager
from django.db.models import Q


# class Permission_user(forms.ModelForm):
#     permissions = PermissionsModelMultipleChoiceField(Permission.objects.none(), widget=forms.CheckboxSelectMultiple)
#     def __init__( self, *args, **kwargs ):
#         super( Permission_user, self ).__init__( *args, **kwargs )
#         ctypes = ContentType.objects.filter(
#             Q(app_label='management') |
#             Q(app_label='auth')
#         )
#         self.fields['permissions'].queryset = Permission.objects.filter(content_type__in=ctypes)

#     class Meta:
#         model = User
#         fields=['permissions']


    # class Meta:
    #     model=User
    #     fields=['permissions']



# class Permission_user(forms.ModelForm):
#     change_user = forms.ChoiceField(
#         widget=forms.RadioSelect,
#         choices=[(True, 'Yes'), (False, 'no')],
#         required=True  # It's required ?
#     )

#     class Meta:
#         model = Profile
#         fields = ('change_user',)

from django.contrib.admin.widgets import FilteredSelectMultiple


class Permission_user(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'permissions': FilteredSelectMultiple("Permission", False, attrs={'rows':'2'}),
        }