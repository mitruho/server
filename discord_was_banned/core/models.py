from django.db import models
class Interest(models.Model):
    interest=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
# Create your models here.
class Project(models.Model):

    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='projectss/')