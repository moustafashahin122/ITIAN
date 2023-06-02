from django.db import models
from course.models import *

# Create your models here.
class trainee(models.Model):
    trainee_id=models.AutoField(primary_key=True,db_column='ID')
    trainee_name=models.CharField(max_length=40,default="trainee")
    email=models.EmailField(max_length=100,default="trainee@gmail.com")
    course_id=models.ForeignKey('course.Course',on_delete=models.CASCADE)
    