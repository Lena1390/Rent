
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('profile')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required
def profile_view(request):
    return render(request, 'profile.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
