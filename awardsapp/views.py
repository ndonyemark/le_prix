from django.shortcuts import render, redirect

def homepage(request):

    title='Homepage'
    context={
        'title':title
    }
    return render(request, 'index.html', context)