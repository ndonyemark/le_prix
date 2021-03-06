from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from awardsapp.models import Project

def user_registration(request):
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('login')
    else:
        registration_form = UserRegistrationForm()
    title='user_registration'
    return render(request, 'users/registration.html', {'title': title,'form': registration_form})

@login_required
def profile(request):
    current_user = request.user
    projects = Project.objects.get(project_owner=request.user)
    return render(request, 'users/profile.html', {'projects': projects})

@login_required
def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm()
    return render(request, 'users/profile_update.html', {'form': form})