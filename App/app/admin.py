from django.contrib import admin
from app.models import PatientFile,PatientJournal,ExternalDocument
# Register your models here.
admin.site.register(PatientJournal)
admin.site.register(ExternalDocument)
admin.site.register(PatientFile)