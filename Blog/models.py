from django.db import models

# Create your models here.
class Blog(models.Model):
    Id = models.AutoField(primary_key=True)
    BlogBame = models.CharField(max_length=50)
    Description = models.TextField()
    HostName = models.CharField(max_length=50)
    DateofPublished = models.DateField()