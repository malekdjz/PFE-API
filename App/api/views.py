from .models import PatientFile,PatientJournal,ExternalDocument
from .serializers import PatientFileSerializer,PatientJournalSerializer,ExternalDocumentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@api_view(['POST'])
def login(request):
    return

@api_view(['POST'])
def logout(request):
    return

@api_view(['GET','POST'])
def patients(request):
    if request.method == 'GET':
        patients = PatientFile.objects.all()
        serializer = PatientFileSerializer(patients,many=True)
        return Response(serializer.data)

    serializer = PatientFileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'details':'invalid data'})

@api_view(['GET','PUT','DELETE'])
def patient(request,pid):
    if request.method == 'GET':
        try:
            patient = PatientFile.objects.get(id=pid)
        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = PatientFileSerializer(patient)

        return Response(serializer.data)
    elif request.method == 'POST':
        return
    return

@api_view(['GET','POST'])
def patient_documents(request,pid):
    if request.method == 'GET':
        documents = ExternalDocument.objects.filter(patient_id=pid)
        serializer = ExternalDocumentSerializer(documents,many=True)
        return Response(serializer.data)
    serializer = ExternalDocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    print(serializer.errors)
    return Response({'details':'Invalid Data'})

@api_view(['GET'])
def patient_document(request,pid,did):
    try:
        document = ExternalDocument.objects.get(patient_id=pid,id=did)
    except ObjectDoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = ExternalDocumentSerializer(document)
    return Response(serializer.data)

@api_view(['GET','POST'])
def patient_journals(request,pid):
    if request.method == 'GET':
        journals = PatientJournal.objects.filter(patient_id=pid)
        serializer = PatientJournalSerializer(journals,many=True)
        return Response(serializer.data)
    return

@api_view(['GET'])
def patient_journal(request,pid,jid):
    try:
        journal = PatientJournal.objects.get(patient_id=pid,id=jid)
    except ObjectDoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = PatientJournalSerializer(journal)
    return Response(serializer.data)