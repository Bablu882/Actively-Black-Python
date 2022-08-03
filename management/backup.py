# def login(request):
#     if request.method=="GET":
#       resp=render(request,'management/login.html')    
#       return resp
#     elif request.method=="POST":
#         u_name=request.POST.get('username')
#         u_pass=request.POST.get('password')
#         p=authenticate(request,username=u_name,password=u_pass)
#         if p is not None:
#             login(request,p)
            
#             return redirect('/profile')
#         else:
#              resp=render(request,'management/login.html')
#              return resp  

#from .forms import SignupForm,UserCreationForm
# def signup_view(request):
#     form=SignupForm(request.POST)

#     if form.is_valid():
    
#         username=form.cleaned_data['username']
#         print(username)
#         email=form.cleaned_datdef login(request):
    # if request.method=="GET":
    #   resp=render(request,'management/login.html')    
    #   return resp
    # elif request.method=="POST":
    #     u_name=request.POST.get('username')
    #     u_pass=request.POST.get('password')
    #     p=authenticate(request,username=u_name,password=u_pass)
    #     if p is not None:
    #         login(request,p)
            
    #         return redirect('/profile')
    #     else:
    #          resp=render(request,'management/login.html')
    #          return resp  

#from .forms import SignupForm,UserCreationForm
# def signup_view(request):a['email']
#         password1=form.cleaned_data['password1']
#         password2=form.cleaned_data['password2']
#         authenticate(username=username,email=email,passowrd1=password1,password2=password2)
#         form.save()
#         return redirect('login')
#         # if new_user is not None:
#         #     login(request,new_user)
#         #     return redirect('login')

        
#     else:
#         form=SignupForm()
#     context={
#         'form':form
#     }    



#     return render(request,'management/register.html',context)


# from django.contrib.auth import get_user_model
# from django_email_verification import SendEmailForVerification

# def logout_user(request):

#     logout(request)

#     messages.add_message(request, messages.SUCCESS,
#                          'Successfully logged out')

#     return redirect(reverse('login'))


# import os
# from django.conf import settings
# from django.shortcuts import render
# from django.templatetags.static import static

# # Create your views here.
# def index(request):
#     path = settings.MEDIA_ROOT
#     img_list = os.listdir(path + '/profile_pics')
#     context = {'images' : img_list}
#     return render(request, "management/profile.html", context)


# @method_decorator(login_required(login_url='login'), name='dispatch')
# class ProfileView(View):
#     profile = None

#     def dispatch(self, request, *args, **kwargs):
#         self.profile, __ = Profile.objects.get_or_create(user=request.user)
#         return super(ProfileView, self).dispatch(request, *args, **kwargs)

#     def get(self, request):
#         context = {'profile': self.profile, 'segment': 'profile'}
#         return render(request, 'management/profile2.html', context)

#     def post(self, request):
#         form = ProfileForm(request.POST, request.FILES, instance=self.profile)

#         if form.is_valid():
#             profile = form.save()
#             profile.user.first_name = form.cleaned_data.get('first_name')
#             profile.user.last_name = form.cleaned_data.get('last_name')
#             profile.user.email = form.cleaned_data.get('email')
#             profile.user.save()

#             messages.success(request, 'Profile saved successfully')
#         else:
#             messages.error(request, form_validation_error(form))
#         return redirect('profile')




# def session_store(request):
#     # …

#     num_authors = User.objects.count()  # The 'all()' is implied by default.

#     # Number of visits to this view, as counted in the session variable.
#     num_visits = request.session.get('num_visits', 0)
#     request.session['num_visits'] = num_visits + 1

#     context = {
#         'num_authors': num_authors,
#         'num_visits': num_visits,
#     }

#     # Render the HTML template index.html with the data in the context variable.
#     return render(request, 'management/dashboard.html', context=context)


# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#         print(ip)
#     return ip



# def activate_user(request, uidb64, token):

#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))

#         user = User.objects.get(pk=uid)

#     except Exception as e:
#         user = None

#     if user and generate_token.check_token(user, token):
#        ## user.is_email_verified = True
#         user.save()

#         messages.add_message(request, messages.SUCCESS,
#                              'Email verified, you can now login')
#         return redirect('/login')

#     return render(request, 'management/activate-fail.html', {"user": user})


# class EmailThread(threading.Thread):

#     def __init__(self, email):
#         self.email = email
#         threading.Thread.__init__(self)

#     def run(self):
#         self.email.send()



# def send_activation_email(user, request):
#     current_site = get_current_site(request)
#     email_subject = 'Activate your account'
#     email_body = render_to_string('management/activate.html', {
#         'user': user,
#         'domain': current_site,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': generate_token.make_token(user)
#     })

    # email = EmailMessage(subject=email_subject, body=email_body,
    #                      from_email=settings.EMAIL_HOST_USER,
    #                      to=[user.email]
    #                      )

    
    # EmailThread(email).start()
#oninvalid="this.setCustomValidity('Valid email required')"  oninput="setCustomValidity('')" required