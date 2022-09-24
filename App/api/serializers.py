from rest_framework import serializers

from .models import PatientFile,PatientJournal,ExternalDocument

class PatientFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientFile
        fields = '__all__'
        read_only_fields = ('created_at','id')

class PatientJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientJournal
        fields = '__all__'
        read_only_fields = ('created_at','id')

class ExternalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalDocument
        fields = '__all__'
        read_only_fields = ('created_at',)