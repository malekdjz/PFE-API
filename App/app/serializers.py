from rest_framework import serializers

from .models import PatientFile,PatientJournal,ExternalDocument

class PatientJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientJournal
        fields = '__all__'
        read_only_fields = ('patient','created_at','id')

class PatientFileSerializer(serializers.ModelSerializer):
    
    url = serializers.HyperlinkedIdentityField(view_name='patient-detail')

    class Meta:
        model = PatientFile
        fields = ('name','last_name','sexe','birth_date','url')
        read_only_fields = ('name','last_name','sexe','birth_date','url')


class PatientFileDetailSerializer(serializers.ModelSerializer):
    
    documents = serializers.HyperlinkedRelatedField(view_name='externaldocument-detail',many=True,read_only=True)
    journal = PatientJournalSerializer(many=True,read_only=True)

    class Meta:
        model = PatientFile
        fields = '__all__'
        read_only_fields = ('user','created_at','id')




class ExternalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalDocument
        fields = '__all__'
        read_only_fields = ('patient','created_at','id') 