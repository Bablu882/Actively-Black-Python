
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models  import Profile


# class SignupForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["username"].widget.attrs.update({
#             'required':'',
#             'name':'username',
#             'id':'username',
#             'type':'text',
#             'class':'form-input',
#             'placeholder':'Username',
#             'maxlength':'50',
#             'minlength':'6'
#         })
#         self.fields["email"].widget.attrs.update({
#             'required':'',
#             'name':'email',
#             'id':'email',
#             'type':'text',
#             'class':'form-input',
#             'placeholder':'Email',
#             'maxlength':'50',
#             'minlength':'6'
#         })
#         self.fields["password1"].widget.attrs.update({
#             'required':'',
#             'name':'password1',
#             'id':'password1',
#             'type':'text',
#             'class':'form-input',
#             'placeholder':'password',
#             'maxlength':'50',
#             'minlength':'6'
#         })
#         self.fields["password2"].widget.attrs.update({
#             'required':'',
#             'name':'password2',
#             'id':'password2',
#             'type':'text',
#             'class':'form-input',
#             'placeholder':'Conform password',
#             'maxlength':'50',
#             'minlength':'6'
#         })
        
        

#     class Meta:
#         model=User
#         fields=['username','email','password1','password2']

# class ProfileForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=255)
#     last_name = forms.CharField(max_length=255)
#     email = forms.EmailField()

#     class Meta:
#         model = Profile
#         fields = '__all__'
#         exclude = ['user']


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg
