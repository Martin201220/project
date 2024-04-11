
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from .models import *


# def home(request):
# 	return render(request, 'home.html')


# def login(request):
	
# 	if request.method == "POST":
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
		
		
# 		if not User.objects.filter(username=username).exists():
		
# 			messages.error(request, 'Invalid Username')
# 			return redirect('/login/')
		
		
# 		user = authenticate(username=username, password=password)
		
# 		if user is None:
			
# 			messages.error(request, "Invalid Password")
# 			return redirect('/login/')
# 		else:
		
# 			login(request, user)
# 			return redirect('/home/')
	
	
# 	return render(request, 'login.html')


# def register(request):
	
# 	if request.method == 'POST':
# 		first_name = request.POST.get('first_name')
# 		last_name = request.POST.get('last_name')
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
		
		
# 		user = User.objects.filter(username=username)
		
# 		if user.exists():
		
# 			messages.info(request, "Username already taken!")
# 			return redirect('/register/')
		
		
# 		user = User.objects.create_user(
# 			first_name=first_name,
# 			last_name=last_name,
# 			username=username
# 		)
		
	
# 		user.set_password(password)
# 		user.save()
		
		
# 		messages.info(request, "Account created Successfully!")
# 		return redirect('/register/')
	
	
# 	return render(request, 'register.html')
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
