from django.shortcuts import render, redirect

def homepage(request):

    title='Homepage'
    context={
        'title':title
    }
    return render(request, 'index.html', context)

def post_project(request):

    title = 'Post Project'
    context={
        'title':title,
    }
    return render(request, 'post_project.html', context)