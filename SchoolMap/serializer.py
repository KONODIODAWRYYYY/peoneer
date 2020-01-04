from rest_framework import serializers
from .models import Room

class RoomSerilizer(serializers.ModelSerializer):
    class Meta:    
        model = Room
        fields = ['name','number', 'floor']
        read_only_fields = fields
        