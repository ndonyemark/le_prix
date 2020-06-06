from django.shortcuts import render, redirect
from .forms import ProjectRegistrationForm
from .models import Project

def homepage(request):
    all_projects = Project.get_all_projects()
    title='Homepage'
    context={
        'title':title,
        'projects': all_projects
    }
    return render(request, 'index.html', context)

def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        project_registration_form = ProjectRegistrationForm(request.POST, request.FILES)
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
        'form': project_registration_form
    }
    return render(request, 'post_project.html', context)