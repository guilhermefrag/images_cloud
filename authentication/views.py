from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def login_redirect(request):
    return redirect('/login/')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user:
                auth_login(request, user)
                
                return redirect('/cloud/home/')
            
            return HttpResponse('Invalid credentials')
        except ValueError as e:
            return HttpResponse(e)

@login_required
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('User already exists')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            return HttpResponse('User created successfully')