from django.urls import path, include
from . import views

urlpatterns = [
    path('lead/', views.LeadListCreate.as_view()),
]