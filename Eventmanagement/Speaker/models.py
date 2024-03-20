from django.db import models

# Create your models here.
class Speaker(models.Model):
    name =models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    biograph = models.TextField(null=True,blank=True)
    profile_pic = models.ImageField(upload_to='speakerphoto/')
    email = models.EmailField()
    socialmedialink = models.URLField()
    phone =models.IntegerField()
   
def __str__(self):
    return self.name