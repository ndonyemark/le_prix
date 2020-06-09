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
    
    title = 'Post Project'
    context={
        'title':title,
    }
    return render(request, 'post_project.html', context)

def single_project(request, project_id):
    single_project = Project.get_single_project(project_id)

    title = single_project.project_title
    context={
        'title': title,
        'project': single_project
    }
    return render(request, 'single_project.html', context)

def search(request):

    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        searched_item = Project.search_by_article(search_term)
        message=f'{search_term}'
        return render(request, 'search.html', { 'message':message, 'search_results':searched_item })

    else:
        message = f'The {search_term} was not found'
    title = 'search item'
    context = {
        'title':title,
        'message': message
    }
    return render(request, 'search.html', context)

def submit_project(request):
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
    
    context={
        'title': 'submit_project',
        'form': project_registration_form
    }

    return render(request, 'submit_project.html', context)