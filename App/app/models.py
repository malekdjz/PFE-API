from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from .validators import validate_file_size
# Create your models here.




class PatientFile (models.Model):

    SEXE_CHOICES = [('m','male'),('f','female')]

    user = models.ForeignKey(User,on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sexe = models.CharField(max_length=1,choices=SEXE_CHOICES)
    birth_date = models.DateField(null=True,blank=True)
    birth_place = models.CharField(max_length=30,null=True,blank=True)
    adress = models.CharField(max_length=100,null=True,blank=True)
    profession = models.CharField(max_length=20,null=True,blank=True)
    phone_number = models.SmallIntegerField(null=True,blank=True)
    room_number = models.SmallIntegerField(null=True,blank=True)
    bed_number = models.SmallIntegerField(null=True,blank=True)
    discharge_date = models.DateField(null=True,blank=True)
    diagnostic = models.TextField(null=True,blank=True)
    medical_history = models.TextField(null=True,blank=True)
    body_exam = models.TextField(null=True,blank=True)
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id) + ": " +self.name + "-" + self.last_name


class ExternalDocument(models.Model):
    patient = models.ForeignKey(PatientFile,on_delete=models.CASCADE)
    image = models.ImageField(validators=[
        FileExtensionValidator(['jpg','png','jpeg']),
        validate_file_size,
        ])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.patient.id) + ": " + self.patient.name + "-" + self.patient.last_name


class PatientJournal(models.Model):
    patient=  models.ForeignKey(PatientFile,on_delete=models.CASCADE)
    locale_treatment = models.TextField(null=True,blank=True)
    general_treatment = models.TextField(null=True,blank=True)
    progress_report = models.TextField(null=True,blank=True)
    complementary_exam = models.TextField(null=True,blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.patient.id) + ": " + self.patient.name + "-" + self.patient.last_name

