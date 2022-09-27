from django.urls import path
from api import views
urlpatterns = [
    path('patients',views.patients),
    path('search/<str:query>',views.advanced_search),
    path('patients/<str:query>',views.search_patient),
    path('patient/<int:pid>',views.patient),
    path('patient/<int:pid>/documents',views.patient_documents),
    path('patient/<int:pid>/document/<int:did>',views.patient_document),
    path('patient/<int:pid>/journals',views.patient_journals),
    path('patient/<int:pid>/journal/<int:jid>',views.patient_journal),
]