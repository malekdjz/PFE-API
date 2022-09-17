from django.urls import path
from api import views
urlpatterns = [
    path('patients',views.patients),
    path('patient/:id',views.patient),
    path('patient/:id/documents',views.patient_documents),
    path('patient/:id/document/:id',views.patient_document),
    path('patient/:id/journals',views.patient_journals),
    path('patient/:id/journal/:id',views.patient_journal),
    path('archives',views.archives),
    path('archives/:id',views.archive),
]