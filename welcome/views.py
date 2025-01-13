from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

# Register view
def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect logged-in users to home
    
    login_form = AuthenticationForm()
    register_form = UserCreationForm()

    if request.method == 'POST':
        # Handle login
        if 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('home')  # Redirect after login
        # Handle registration
        elif 'register' in request.POST:
            register_form = UserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('home')  # Redirect after registration

    return render(request, 'welcome.html', {
        'login_form': login_form,
        'register_form': register_form,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('home')  # Redirect to home after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})