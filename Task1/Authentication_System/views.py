from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.http import HttpResponseForbidden
# Signup view
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Create a new user
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            auth_login(request, user)  # Log the user in automatically after signup
            messages.success(request, "You have successfully signed up!")
            return redirect('home')  # Redirect to home page after signup
    else:
        form = SignUpForm()

    return render(request, 'Authentication_System/signup.html', {'form': form})

# Login view
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect('home')  # Redirect to home page after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please provide valid credentials.")
    else:
        form = LoginForm()

    return render(request, 'Authentication_System/login.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        messages.success(request, "You have successfully logged out!")
        return redirect('login')  # Redirect to login page after logout
    else:
        return HttpResponseForbidden("Forbidden: Only POST method is allowed for logout.")

# Home page (protected view)
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if the user is not logged in
    return render(request, 'Authentication_System/home.html')
