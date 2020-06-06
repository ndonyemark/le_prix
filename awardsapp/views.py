from django.shortcuts import render, redirect
from .forms import ProjectRegistrationForm

def homepage(request):

    title='Homepage'
    context={
        'title':title
    }
    return render(request, 'index.html', context)

def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        project_registration_form = ProjectRegistrationForm(request.POST)
        if project_registration_form.is_valid():
            project = project_registration_form.save(commit=False)
            project.project_owner = current_user
            project.save()
            return redirect('post_project')
    else:
        project_registration_form = ProjectRegistrationForm()
    title = 'Post Project'
    context={
        'title':title,
    }
    return render(request, 'post_project.html', context)