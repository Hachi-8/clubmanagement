from datetime import datetime
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from registration.models import UserDetail
from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    groupid = models.IntegerField(primary_key=True)
    schoolname = models.CharField(max_length=20)
    leadername = CharField(max_length=20)


class Conditions(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField()        #(verbose_name = "conditionSavedTime", auto_now=True, auto_now_add=False)
    bodyTemperature = models.FloatField()
    cough = models.CharField(max_length=2)  #ありorなし
    dyspnea = models.CharField(max_length=2)  #ありorなし
    soreThroat = models.CharField(max_length=2)  #ありorなし
    malaise = models.CharField(max_length=2)  #ありorなし
    abnormalTasteAndSmell = models.CharField(max_length=2)  #ありorなし
    other = models.CharField(max_length=100)

class freeThrough(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    attempt = models.IntegerField()
    make = models.IntegerField()

class threeMen(models.Model):
    date = models.DateField()
    attempt = models.IntegerField()
    make = models.IntegerField()
    accomplish = models.CharField(max_length=3)

class MatchResult(models.Model):
    date = models.DateField()
    icu_total = models.IntegerField()       
    icu_1Q = models.IntegerField()
    icu_2Q = models.IntegerField()
    icu_3Q = models.IntegerField()
    icu_4Q = models.IntegerField()
    op_team= models.CharField(max_length=15)
    op_total = models.IntegerField()  
    op_1Q = models.IntegerField()
    op_2Q = models.IntegerField()
    op_3Q = models.IntegerField()
    op_4Q = models.IntegerField()

class MatchResultDetail(models.Model):
    name = models.ForeignKey(User, on_delete=CASCADE)
    date = models.ForeignKey("MatchResult",on_delete=CASCADE, related_name="match_date")
    op_team = models.ForeignKey("MatchResult", on_delete=CASCADE, related_name="opponent_team")
    points = models.IntegerField()
    underGoalAttempt = models.IntegerField()
    underGoalIn = models.IntegerField()
    middleAttempt = models.IntegerField()
    middleIn = models.IntegerField()
    threePointAttempt = models.IntegerField()
    threePointIn = models.IntegerField()
    faul = models.IntegerField(default=0)
    turnOver = models.IntegerField(default=0)

class Shooting(models.Model):
    name = ForeignKey(User, on_delete=CASCADE)
    date = models.DateField(default=datetime.today())
    attempt = models.IntegerField()
    make = models.IntegerField()