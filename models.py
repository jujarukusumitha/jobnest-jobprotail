from django.db import models

class Hrdetails(models.Model):  # Correct 'model' to 'models.Model'
    Id = models.IntegerField(primary_key=True)
    Companyname = models.CharField(max_length=100)
    Vacancys = models.IntegerField()
    Role = models.CharField(max_length=100)
    Package = models.IntegerField()
    Experience = models.IntegerField()
    Skills = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Startdate = models.DateField()
    Deadline = models.DateField()
    Phonenumber = models.BigIntegerField()


