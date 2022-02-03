from django.db import models

# Create your models here.
class students(models.Model):
    id = models.AutoField( primary_key=True)
    username = models.CharField(max_length=40)
    # email = models.EmailField()
    password = models.CharField(max_length=60)


class Intake(models.Model):
    intakeName = models.CharField(max_length=40)
    id = models.AutoField(primary_key=True)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
