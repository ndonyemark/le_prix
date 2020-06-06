from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def user_registration(request):
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('login')
    else:
        registration_form = UserRegistrationForm()
    title='user_registration'
    context={
        'title': title,
    }
    return render(request, 'users/registration.html', context)