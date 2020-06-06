from django import forms
from .models import Project

class ProjectRegistrationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_title', 'project_description', 'project_live_link', 'project_image']