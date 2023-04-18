from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['pk', 'name', 'protagonists', 'poster', 'started_at', 'status', 'ranking']
