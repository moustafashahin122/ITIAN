from django.db import models

# Create your models here.
class MyUser(models.Model):
    id=models.AutoField(primary_key=True,db_column='ID')
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    active=models.BooleanField()
