from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post_project', views.post_project, name='post_project'),
    path('single_project/<int:project_id>', views.single_project, name='single_project'),
    path('search', views.search, name='search'),
    path('submit_project', views.submit_project, name='submit_project'),
    path('api/profile', views.ProfileList.as_view()),
    path('api/profile/profile_id/<int:pk>', views.ProfileDescription.as_view())
]
