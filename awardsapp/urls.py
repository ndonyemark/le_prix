from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post_project', views.post_project, name='post_project'),
    path('single_project/<int:project_id>', views.single_project, name='single_project')
]
