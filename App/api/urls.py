from django.urls import path
from api import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('login',views.login),
    path('logout',views.logout),
    path('patients',views.patients),
    path('patient/<int:pid>',views.patient),
    path('patient/<int:pid>/documents',views.patient_documents),
    path('patient/<int:pid>/document/<int:did>',views.patient_document),
    path('patient/<int:pid>/journals',views.patient_journals),
    path('patient/<int:pid>/journal/<int:jid>',views.patient_journal),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # <---- this is for developement only
