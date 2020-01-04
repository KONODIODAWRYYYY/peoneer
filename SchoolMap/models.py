from django.db import models

# Create your models here.
decode = {33:"кз", 34:"фз", 35:"фз"}

class Room(models.Model):
    ROOM_CHOICES = [ (key, key) for key in range (1,36)]
    name = models.CharField(max_length = 20, default = "Кабинет общего назначения")
    number = models.SmallIntegerField(choices = ROOM_CHOICES, default = 1)
    floor = models.SmallIntegerField(default = 1)
    
    class Meta:
        ordering = ['floor', '-number']
    
    def __str__(self):
        return self.decode_number()
    
    def decode_number(self):
        if self.number in [34,35,33]:
            return decode[self.number]
        return str(self.number)