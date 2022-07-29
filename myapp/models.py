from django.db import models

# Create your models here.
class Data(models.Model):
    email = models.EmailField(max_length=20)
    name = models.TextField(max_length=20)
    password = models.CharField(max_length=20)

    
