from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Patient (models.Model):

    SEXE_CHOICES = [('m','male'),(('f','female'))]

    user = models.ForeignKey(User,on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sexe = models.CharField(max_length=1,choices=SEXE_CHOICES)
    birth_date = models.DateField(null=True,blank=True,default=NULL)
    birth_place = models.CharField(max_length=30,null=True,blank=True,default=NULL)
    adress = models.CharField(max_length=100,null=True,blank=True,default=NULL)
    profession = models.CharField(max_length=20,null=True,blank=True,default=NULL)
    phone_number = models.SmallIntegerField(null=True,blank=True,default=NULL)
    room_number = models.SmallIntegerField(null=True,blank=True,default=NULL)
    bed_number = models.SmallIntegerField(null=True,blank=True,default=NULL)
    entry_date = models.DateField()
    discharge_date = models.DateField(null=True,blank=True,default=NULL)
    diagnostic = models.TextField(null=True,blank=True,default=NULL)
    medical_history = models.TextField(null=True,blank=True,default=NULL)
    body_exam = models.TextField(null=True,blank=True,default=NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['id']

class Archive(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sexe = models.CharField(max_length=1)
    birth_date = models.DateField(null=True,blank=True)
    birth_place = models.CharField(max_length=30,null=True,blank=True)
    adress = models.CharField(max_length=100,null=True,blank=True)
    proffesion = models.CharField(max_length=20,null=True,blank=True)
    phone_number = models.SmallIntegerField(null=True,blank=True)
    room_number = models.SmallIntegerField(null=True,blank=True)
    bed_number = models.SmallIntegerField(null=True,blank=True)
    entry_date = models.DateField()
    discharge_date = models.DateField(null=True,blank=True)
    diagnostic = models.TextField(null=True,blank=True)
    medical_history = models.TextField(null=True,blank=True)
    body_exam = models.TextField(null=True,blank=True)
    archived_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField()

    class meta:
        ordering = ['id']

class ExternalDocument(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    link = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    class meta:
        ordering = ['id']

class PatientJournal(models.Model):
    patient=  models.ForeignKey(Patient,on_delete=models.CASCADE)
    locale_treatment = models.TextField(null=True,blank=True)
    general_treatment = models.TextField(null=True,blank=True)
    progress_report = models.TextField(null=True,blank=True)
    complementary_exam = models.TextField(null=True,blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['id']