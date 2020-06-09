from rest_framework import serializers
from .models import ApiProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiProfile
        fields = ['id', 'username', 'bio', 'profile_picture']