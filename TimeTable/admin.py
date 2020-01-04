from django.contrib import admin
from .models import Lesson
# Register your models here.
class LessonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('время', {'fields': ['day', 'time']}),
        ("описание предмета", {'fields': ['name', 'course', 'room']}),
    ]
    list_display = ('name','day', 'course', 'time')
admin.site.register(Lesson, LessonAdmin)
