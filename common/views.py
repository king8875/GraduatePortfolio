from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm, UserUpdateForm, ProfileUpdateForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile 
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import serializers
from .serializer import UserSerializer


class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('common:edit_profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'common/edit_profile.html', {'form': form})






def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('pybo:index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def landing(request):
    
    return render(request, 'common/landing.html')