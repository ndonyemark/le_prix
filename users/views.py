from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileUpdateForm
from .models import Profile

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

def profile(request):
    current_user = request.user
    # user_profile_data = Profile.get_user_profile_data(current_user)
    return render(request, 'users/profile.html')

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