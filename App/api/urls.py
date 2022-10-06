from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('patients',views.Patients.as_view(),name='patients'),
    path('patient/<int:pid>',views.Patient.as_view(),name='patient'),
    path('patient/<int:pid>/documents',views.PatientDocuments.as_view(),name='documents'),
    path('patient/<int:pid>/document/<int:did>',views.PatientDocument.as_view(),name='document'),
    path('patient/<int:pid>/journals',views.PatientJournals.as_view(),name='journals'),
    path('patient/<int:pid>/journal/<int:jid>',views.PatientJournal.as_view(),name='journal'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout',views.Logout.as_view(),name='logout'),
]
