from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm, ShopUserProfileEditForm
from authapp.models import User
from basket.models import Basket
from .utils import send_verify_mail
from django.db import transaction


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
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            send_verify_mail(user)
            messages.success(request, 'Проверьте почту')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.userprofile
                                               )
    context = {
        'form': form,
        'profile_form': profile_form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'authapp/profile.html', context)


def verify(request, user_id, hash):
    user = get_object_or_404(User, pk=user_id)
    # user = User.objects.get(pk=user_id)
    if user.activation_key == hash and not user.is_activation_key_expired():
        user.is_active = True
        user.activation_key = None
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return render(request, 'authapp/verification.html')

# @transaction.atomic
# def edit(request):
#     title = 'редактирование'
#
#     if request.method == 'POST':
#         edit_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
#         profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.userprofile)
#         if edit_form.is_valid() and profile_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('auth:edit'))
#     else:
#         edit_form = ShopUserEditForm(instance=request.user)
#         profile_form = ShopUserProfileEditForm(
#             instance=request.user.userprofile
#         )
#
#     content = {
#         'title': title,
#         'edit_form': edit_form,
#         'profile_form': profile_form
#     }
#
#     return render(request, 'authapp/edit.html', content)
