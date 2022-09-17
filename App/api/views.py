from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Patient,Archive,PatientJournal,ExternalDocument
from .serializers import PatientSerializer,ArchiveSerializer,PatientJournalSerializer,ExternalDocumentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def patients(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients,many=True)
        return Response(serializer.data)
    return

@api_view(['GET','PUT','DELETE'])
def patient(request,pid):
    if request.method == 'GET':
        patient = Patient.objects.get(id=pid)
        serializer = PatientSerializer(patient)
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
    return

@api_view(['GET'])
def patient_document(request,pid,did):
    document = ExternalDocument.objects.get(patient_id=pid,id=did)
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
    journal = PatientJournal.objects.get(patient_id=pid,id=jid)
    serializer = PatientJournalSerializer(journal)
    return Response(serializer.data)

@api_view(['GET'])
def archives(request):
    archives = Archive.objects.all()
    serializer = ArchiveSerializer(archives,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def archive(request,aid):
    archive = Archive.objects.get(id=aid)
    serializer = ArchiveSerializer(archive)
    return Response(serializer.data)