from app.models import *
from app.serializers import *
from app.models import PatientFile,PatientJournal,ExternalDocument
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.views  import APIView
from .myfuncs import sanitize,validate_orderby,validate_date
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse
from django.conf import settings

# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        groups = user.groups.values_list('name',flat=True)
        roles = list(groups)
        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_ame'] = user.last_name
        token['email'] = user.email
        token['roles'] = roles
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class Logout(APIView):
    def post(self,request):
        try:
            token = request.data['refresh']
            RefreshToken(token).blacklist()
            return Response(status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status.HTTP_400_BAD_REQUEST)




class Patients(APIView):
    queryset = User.objects.none()
    def get(self,request):
        params = request.GET
        query = sanitize(params.get('q',''))
        order = params.get('o','')
        ascending = params.get('asc','')
        entry = params.get('e','')
        discharge = params.get('d','')
        born_after = params.get('ba','')
        born_before = params.get('bb','')
        archived = params.get('a','')
        sexe = params.get('s','')
        user = params.get('u','')

        q = PatientFile.objects.filter(Q(name__icontains=query)|
        Q(last_name__icontains=query)|
        Q(adress__icontains=query)|
        Q(birth_place__icontains=query)
        )
        if sexe == "m"or sexe =="f":
            q = q.filter(sexe=sexe)
        if archived == "true":
            q = q.filter(archived=True)
        elif archived == "false":
            q = q.filter(archived=False)
        if validate_date(born_after):
            q = q.filter(birth_date__gte = born_after)
        if validate_date(born_before):
            q = q.filter(birth_date__lte = born_before)
        if validate_date(entry):
            q = q.filter(created_at__gte = entry)
        if validate_date(discharge):
            q = q.filter(discharge_date__lte = discharge)
        if validate_orderby(order):
            if ascending :
                q = q.order_by(order)
            else:
                q= q.order_by('-'+order)
        if user:
            q = q.filter(user_id=user)
        paginate = PageNumberPagination()
        results = paginate.paginate_queryset(queryset=q,request=request)
        serializer = PatientFileSerializer(results,many=True,context={'request':request})
        response = paginate.get_paginated_response(data=serializer.data)
        return response

    def post(self,request):
        serializer = PatientFileDetailSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status.HTTP_200_OK)
        print(serializer.errors)
        return Response({'detail':'invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)


class PatientsDetail(APIView):
    queryset = User.objects.none()
    def get(self,request,pk):
        try:
            patient = PatientFile.objects.get(id=pk)
        except:
            return Response({'detail':'patient file does not exist'},status.HTTP_404_NOT_FOUND)
        serializer = PatientFileDetailSerializer(patient,context={'request':request})
        response = serializer.data
        response['user_first_name'] = patient.user.first_name
        response['user_last_name'] = patient.user.last_name
        return Response(response,status.HTTP_200_OK)

    def put(self,request,pk):
        try:
            patient = PatientFile.objects.get(id=pk)
        except:
            return Response({'detail':'patient file does not exist'},status.HTTP_404_NOT_FOUND)
        if not patient.archived:
            serializer = PatientFileDetailSerializer(patient,data=request.data,partial=True,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status.HTTP_200_OK)
            print(serializer.errors)
            return Response({'detail':'invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        return Response({'detail':'file is archived'},status.HTTP_403_FORBIDDEN)


class PatientDocumentsDetail(APIView):
    queryset = User.objects.none()
    def get(self,request,pk):
        try:
            document = ExternalDocument.objects.get(id=pk)
        except:
            return Response({'detail':'document does not exist'},status.HTTP_404_NOT_FOUND)
        serializer = ExternalDocumentSerializer(document)
        p = str(settings.MEDIA_ROOT)+ serializer.data['image']
        content_type = 'image/png'
        if not serializer.data['image'].endswith('.png'):
            content_type = 'image/jpeg'
        file = open(p,'rb')
        return HttpResponse(file,content_type=content_type,status=status.HTTP_200_OK)


class PatientDocuments(APIView):
    queryset = User.objects.none()
    def get(self,request,pk):
        documents = ExternalDocument.objects.filter(patient_id=pk)
        serializer = ExternalDocumentSerializer(documents,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self,request,pk):
        try:
            patient = PatientFile.objects.get(id=pk)
        except:
            return Response({'detail':'patient file does not exist'},status.HTTP_404_NOT_FOUND)
        if not patient.archived:
            serializer = ExternalDocumentSerializer(data=request.data)
            if serializer.is_valid(patient=patient):
                serializer.save()
                return Response(serializer.data,status.HTTP_200_OK)
            return Response({'detail':'invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        return Response({'detail':'file is archived'},status.HTTP_403_FORBIDDEN)


class PatientJournals(APIView):
    queryset = User.objects.none()
    def get(self,request,pk):
        journals = PatientJournal.objects.filter(patient_id=pk)
        serializer = PatientJournalSerializer(journals,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

    def post(self,request,pk):    
        try:
            patient = PatientFile.objects.get(id=pk)
        except:
            return Response({'detail':'patient file does not exist'},status.HTTP_404_NOT_FOUND)
        if not patient.archived:
            serializer = PatientJournalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(patient=patient)
                return Response(serializer.data,status.HTTP_200_OK)
            print(serializer.errors)
            return Response({'detail':'invalid data'},status.HTTP_422_UNPROCESSABLE_ENTITY)
        return Response({'detail':'file is archived'},status.HTTP_403_FORBIDDEN)
    

class PatientJournalsDetail(APIView):
    queryset = User.objects.none()
    def get(self,request,pk):
        try:
            journal = PatientJournal.objects.get(id=pk)
        except:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = PatientJournalSerializer(journal)
        return Response(serializer.data,status.HTTP_200_OK)
