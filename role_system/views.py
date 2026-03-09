from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render (request, 'role_system/index.html')

def employer(request):
    return render (request, 'role_system/employer.html')