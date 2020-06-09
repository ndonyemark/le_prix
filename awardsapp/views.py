from django.shortcuts import render, redirect
from .forms import ProjectRegistrationForm
from .models import Project
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ApiProfile
from .serializers import ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

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

@login_required
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

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = ApiProfile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        permission_classes = (IsAdminOrReadOnly)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly)
    def get_profile(self, pk):
        try:
            return ApiProfile.objects.get(pk=pk)
        except ApiProfile.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)