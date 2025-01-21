from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/')
    url = models.URLField()

    def __str__(self):
        return self.name
# class Projec(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
    
class Mynews(models.Model):
    title = models.CharField(primary_key=True, max_length=200)
    image = models.ImageField(upload_to='mynews_images/')
    pdf= models.FileField(upload_to='mynews_pdfs/', null=True, blank=True)


  