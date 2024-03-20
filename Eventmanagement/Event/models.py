from django.db import models
from Speaker.models import Speaker

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

    

class Event(models.Model):
    title=models.CharField(max_length=200)
    description= models.TextField(null=True,blank=True)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isfree = models.BooleanField()
def __str__(self):
    return self.title

class Schedule(models.Model):
        topic=models.CharField(max_length=200)
        startDate=models.DateTimeField()
        endDate=models.DateTimeField()
        speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
        def __str__(self) :
            return self.topic