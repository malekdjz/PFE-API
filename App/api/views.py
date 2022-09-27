from wsgiref import validate
from .models import PatientFile,PatientJournal,ExternalDocument
from .serializers import PatientFileSerializer,PatientSerializer,PatientJournalSerializer,ExternalDocumentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q
from .myfuncs import sanitize,validate_orderby,validate_date
# Create your views here.

@api_view(['POST'])
def login(request):
    #TODO use jwt for auth
    return

@api_view(['POST'])
def logout(request):
    return

@api_view(['GET'])
def advanced_search(request):
    #TODO : this function is to be removed
    params = request.GET
    query = sanitize(params.get('q'),'')
    order = sanitize(params.get('o'),'')
    ascending = sanitize(params.get('a'),'')
    entry = sanitize(params.get('e'),'')
    discharge = sanitize(params.get('d'),'')
    birth = sanitize(params.get('b'),'')

    q = PatientFile.objects.filter(Q(name__conatins=query)|
        Q(last_name__contains=query)|
        Q(adress__contains=query)|
        Q(birth_place__contains=query)
        )
    if validate_orderby(order):
        pass
    return

@api_view(['GET'])
def search_patient(request,query):
    #TODO : this function is to be removed
    query = sanitize(query)
    patients = PatientFile.objects.filter(Q(name__contains=query)|Q(last_name__contains=query))
    serializer = PatientSerializer(patients,many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def patients(request):
    if request.method == 'GET':
        #TODO : finish and test whatever this is
        params = request.GET
        query = sanitize(params.get('q',''))
        order = params.get('o','')
        ascending = params.get('a','')
        entry = params.get('e','')
        discharge = params.get('d','')
        birth = params.get('b','')

        q = PatientFile.objects.filter(Q(name__conatins=query)|
        Q(last_name__contains=query)|
        Q(adress__contains=query)|
        Q(birth_place__contains=query)
        )

        if validate_date(birth):
            q = q.filter(birth_date = birth)
        
        if validate_date(entry):
            q = q.filter(created_at__gte = entry)

        if validate_date(discharge):
            q = q.filter(discharge_date__lte = discharge)

        if validate_orderby(order):
            if ascending :
                q = q.order_by(order)
            else:
                q= q.order_by('-'+order)

        serializer = PatientFileSerializer(q,many=True)
        return Response(serializer.data)

    serializer = PatientFileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'details':'invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['GET','PUT'])
def patient(request,pid):
    if request.method == 'GET':
        try:
            patient = PatientFile.objects.get(id=pid)
        except:
            return Response({'details':'patient file does not exist'},status.HTTP_404_NOT_FOUND)
        serializer = PatientFileSerializer(patient)
        return Response(serializer.data)

    try:
        patient = PatientFile.objects.get(id=pid)
    except:
        return Response({'details':'patient file does not exist'},status.HTTP_404_NOT_FOUND)
    if not patient.archived:
        serializer = PatientFileSerializer(patient,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response({'details':'invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({'details':'file is archived'},status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def patient_document(request,pid,did):
    try:
        document = ExternalDocument.objects.get(patient_id=pid,id=did)
    except:
        return Response({'details':'document does not exist'},status.HTTP_404_NOT_FOUND)
    serializer = ExternalDocumentSerializer(document)
    return Response(serializer.data)

@api_view(['GET','POST'])
def patient_documents(request,pid):
    if request.method == 'GET':
        documents = ExternalDocument.objects.filter(patient_id=pid)
        serializer = ExternalDocumentSerializer(documents,many=True)
        return Response(serializer.data)
    
    try:
        patient = PatientFile.objects.get(id=pid)
    except:
        return Response({'details':'patient file does not exist'},status.HTTP_404_NOT_FOUND)
    if not patient.archived:
        serializer = ExternalDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'details':'invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({'details':'file is archived'},status.HTTP_403_FORBIDDEN)

@api_view(['GET','POST'])
def patient_journals(request,pid):
    if request.method == 'GET':
        journals = PatientJournal.objects.filter(patient_id=pid)
        serializer = PatientJournalSerializer(journals,many=True)
        return Response(serializer.data)
    try:
        patient = PatientFile.objects.get(id=pid)
    except:
        return Response({'details':'patient file does not exist'},status.HTTP_404_NOT_FOUND)
    if not patient.archived:
        serializer = PatientJournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'details':'invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({'details':'file is archived'},status.HTTP_403_FORBIDDEN)
    


@api_view(['GET'])
def patient_journal(request,pid,jid):
    try:
        journal = PatientJournal.objects.get(patient_id=pid,id=jid)
    except:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = PatientJournalSerializer(journal)
    return Response(serializer.data)