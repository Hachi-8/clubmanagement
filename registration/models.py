from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField
from django.contrib.auth.models import User
# Create your models here.

class UserDetail(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.IntegerField()
    schoolId = models.IntegerField()
    position = models.CharField(max_length = 6)