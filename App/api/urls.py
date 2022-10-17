from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('patients/',views.Patients.as_view(),name='patient'),
    path('patient/<int:pk>/',views.PatientsDetail.as_view(),name='patient-detail'),

    path('patient/<int:pk>/documents/',views.PatientDocuments.as_view(),name='externaldocument'),
    path('document/<int:pk>/',views.PatientDocumentsDetail.as_view(),name='externaldocument-detail'),

    path('patient/<int:pk>/journals/',views.PatientJournals.as_view(),name='patientjournal'),
    path('journal/<int:pk>/',views.PatientJournalsDetail.as_view(),name='patientjournal-detail'),
    
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',views.Logout.as_view(),name='logout'),
]
