from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout
from aviaweb.models import *
from django.contrib.auth import update_session_auth_hash


def log_in(request):
    form = SignInForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)

        if request.GET.get('next'):
            return redirect(request.GET.get('next'))


        return redirect('aviaweb:home')
    return render(request, 'log_in.html', {'form': form})


def log_reg(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('users:log_in')
    return render(request, 'log_reg.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('users:log_in')


def edit_profile(request):
    form = EditProfileForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('aviaweb:home')
    return render(request, 'edit_profile.html', {'form': form})


def reset_password(request):
    form = ResetPasswordForm(request.user, request.POST or None)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('users:log_in')
    return render(request, 'reset_password.html', {'form': form})

