from django.shortcuts import render, redirect
from .models import Customuser, RecruiterProfile, JobSeekerProfile

# Create your views here.
def home(request):
    return render (request, 'role_system/index.html')

def register(request):
    return render (request, 'role_system/register.html')

def log_in(request):
    return render (request, 'role_system/login.html')