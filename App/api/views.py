from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Patient
from .serializers import PatientSerializer
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
def patient(request):
    if request.method == 'GET':
        return
    elif request.method == 'POST':
        return
    return

@api_view(['GET','POST'])
def patient_documents(request):
    if request.method == 'GET':
        return
    return

@api_view(['GET'])
def patient_document(request):
    return

@api_view(['GET','POST'])
def patient_journals(request):
    if request.method == 'GET':
        return
    return

@api_view(['GET'])
def patient_journal(request):
    return

@api_view(['GET'])
def archives(request):
    return

@api_view(['GET'])
def archive(request):
    return