from django.db import models
from SchoolMap.models import Room
from .utils import days, classes, decode_course
# Create your models here.
    
class Lesson(models.Model):
    DAY_CHOICES = [ (i, days[i]) for i in range(6) ]
    CLASS_CHOICES = [ (item, decode_course(item)) for item in classes ]
    
    name =  models.CharField(max_length = 30, default = '')
    time = models.TimeField()
    day = models.SmallIntegerField(choices = DAY_CHOICES)
    course = models.SmallIntegerField(choices = CLASS_CHOICES,
                                      default=0
                                     )
    room = models.ForeignKey(Room,
                             models.SET_NULL, 
                             blank = True, 
                             null = True,
                            )
    is_extra = models.BooleanField(default = False)
    class Meta:
        ordering = ['-day', 'course', 'time']

    def __str__(self):
        return self.name