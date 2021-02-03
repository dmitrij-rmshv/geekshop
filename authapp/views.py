from django.shortcuts import render, HttpResponseRedirect

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.urls import reverse


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            form = UserLoginForm()
        context = {'form': form}
    return render(request, 'authapp/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
        else:
            form = UserRegisterForm()
        context = {'form': form}
    return render(request, 'authapp/register.html')


def logout(request):
    auth.logout(request)
    return  HttpResponseRedirect(reverse('index'))


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'authapp/profile.html')
