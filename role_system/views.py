# import necessary modules 
from django.shortcuts import render, redirect, get_object_or_404
# render → use to render HTML template with context
# redirect → use to redirect user to another URL
# get_object_or_404 → to fetch a single object from database.

from .models import Customuser, RecruiterProfile, JobSeekerProfile # import your custom models

from django.contrib import messages # Django messages framework for success/error notifications

from django.contrib.auth import authenticate, login, logout
# authenticate → check username/password
# login → log user in (create session)
# logout → log user out (destroy session)


def home(request):
    return render(request, 'role_system/index.html')
    # just render the homepage template
    # no context needed

def register(request):

    if request.method == "POST": # check if form submitted via POST

        # Get data from HTML form
        user_name = request.POST.get('username')            # username input
        full_name = request.POST.get('fullname')            # full name input
        mail = request.POST.get('email')                    # email input
        role = request.POST.get('role')                     # role selection (recruiter/jobseeker)
        pro_pic = request.FILES.get('profile_photo')        # profile photo upload
        pass_word = request.POST.get('password')            # password input
        confrim_password = request.POST.get('re_password')  # confirm password input

        # Password check
        if pass_word != confrim_password:
            messages.error(request, 'Password unmatched')   # show error if passwords don't match
            return redirect('register')                     # redirect back to register page

        # Username exists check
        if Customuser.objects.filter(username = user_name).exists():
            messages.error(request, 'username already exists')
            return redirect('register')   # redirect back to register page

        # Email exists check
        if Customuser.objects.filter(email = mail).exists():
            messages.error(request, 'email already exists')
            return redirect('register')    # redirect back to register page

        # create_user → automatically hashes the password
        user = Customuser.objects.create_user(
            username = user_name,
            email = mail,
            password = pass_word
        )

        user.profile_pic = pro_pic   # set uploaded profile picture
        user.role = role             # set role
        
        if role == "recruiter":
            RecruiterProfile.objects.create(user = user)     #  creates a recruiter profile object linked to the user
        
        elif role == "job_seeker":
            JobSeekerProfile.objects.create(user = user)     #  creates a job seeker profile object linked to the user
            
        user.save()                  # save the user object to database

            
        messages.success(request, 'registration successfull')
        return redirect('login')     # redirect to login page

    # show register form
    return render(request, 'role_system/register.html')

def log_in(request):

    if request.method == "POST": # Get form input
        
        user_input = request.POST.get('email_username')   # user can enter email or username
        pass_word = request.POST.get('password')          # password input

        # Check if input is email
        try:
            user_obj = Customuser.objects.get(email = user_input)
            # user_obj → fetch user object from Customuser model where email = username_mail
            user_input = user_obj.username     # if email exists → get the corresponding username
        except Customuser.DoesNotExist:
            user_name = user_input             # if email does not exist, input was username

        # Authenticate user
        user = authenticate(request, username = user_name, password = pass_word)
        # authenticate → returns user object if username & password correct

        # Login user if authenticated
        if user is not None:
            login(request, user)                            # log the user in (create session)
            messages.success(request, "Login Successful")   # show success message
            return redirect('home')                    
        else:
            messages.error(request, "Invalid Credentials") # show error if login fails

    # GET request → show login form
    return render(request, 'role_system/login.html') 

def log_out(request):
    
    logout(request)
    messages.success(request, 'logout suceess')
    
    return redirect('login')