from django.urls import path
from api import views
urlpatterns = [
    path('patients',views.patients),
    path('patient/<int:pid>/',views.patient),
    path('patient/<int:pid>/documents',views.patient_documents),
    path('patient/<int:pid>/document/<int:did>',views.patient_document),
    path('patient/<int:pid>/journals',views.patient_journals),
    path('patient/<int:pid>/journal/<int:jid>',views.patient_journal),
    path('archives',views.archives),
    path('archives/<int:aid>/',views.archive),
]