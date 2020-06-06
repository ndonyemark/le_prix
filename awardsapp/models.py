from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    project_title = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='project_pics')
    project_description = models.TextField()
    project_live_link = models.CharField(max_length=100)
    project_pub_date = models.DateTimeField(auto_now_add=True)
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_title
