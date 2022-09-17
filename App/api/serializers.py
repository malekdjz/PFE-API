from rest_framework import serializers

from .models import Patient,Archive,PatientJournal,ExternalDocument

class PatientSerializer(serializers.Serializer):
    class meta:
        model = Patient
        fields = '__all__'
    
class ArchiveSerializer(serializers.Serializer):
    class meta:
        model = Archive
        fields = '__all__'

class PatientJournalSerializer(serializers.Serializer):
    class meta:
        model = PatientJournal
        fields = '__all__'

class ExternalDocumentSerializer(serializers.Serializer):
    class meta:
        model = ExternalDocument
        fields = '__all__'