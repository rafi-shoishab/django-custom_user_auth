from django.shortcuts import render, redirect
from .models import Customuser, RecruiterProfile, JobSeekerProfile
from django.contrib import messages

# Create your views here.
def home(request):
    return render (request, 'role_system/index.html')

def register(request):

    if request.method == "POST":
        user_name = request.POST.get('username')
        full_name = request.POST.get('fullname')
        mail = request.POST.get('email')
        role = request.POST.get('role')
        pro_pic = request.FILES.get('profile_photo')
        pass_word = request.POST.get('password')
        confrim_password = request.POST.get('re_password')

        if pass_word != confrim_password:
            messages.error(request, 'Password unmatched')
            return redirect('register')
        
        if Customuser.objects.filter(username = user_name).exists():
            messages.error(request, 'username already exists')
            return redirect('register')
        
        if Customuser.objects.filter(email = mail).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        
        user = Customuser.objects.create_user(
            username = user_name,
            email = mail,
            password = pass_word 
        )

        user.profile_pic = pro_pic
        user.role = role

        user.save()
        messages.success(request, 'registration successfull')
        return redirect ('login')

    return render (request, 'role_system/register.html')

def log_in(request):
    return render (request, 'role_system/login.html')