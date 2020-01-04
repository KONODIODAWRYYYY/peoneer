from rest_framework import serializers
from .models import Introduce

class IntroduceSerializer(serializers.ModelSerializer):
    fields = ['authors', 'title', 'text']
    read_only_fields = fields