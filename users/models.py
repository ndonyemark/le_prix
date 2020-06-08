from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile_pics')
    profile_bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @classmethod
    def get_user_profile_data(cls, user_name):
        user_data = Profile.objects.get(user = user_name)