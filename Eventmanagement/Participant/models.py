from django.db import models
from Event.models import Event
# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phoneNumber = models.IntegerField()
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name