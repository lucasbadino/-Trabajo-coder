from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    Dni= models.IntegerField(default="unknow")
    date_of_birth = models.DateField(auto_now_add=True, blank=True, null=True)
    age= models.DateField(auto_now_add=True, blank=True, null=True)