from django.shortcuts import render

def user_registration(request):

    title='user_registration'
    context={
        'title': title,
    }
    return render(request, 'users/registration.html', context)