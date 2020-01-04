from rest_framework import serializers
from .models import Lesson

class LessonSerializer(serializers.ModelSerializer):
	"""
		сериализатор, преобразующий данные БД
		в json
	"""
	class Meta:
		model = Lesson
		fields = ["day", "course", "time", "name", "room"]
		read_only_fields = fields