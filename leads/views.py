from django.shortcuts import render
from .seraializers import LeadSearializer
from .models import Lead

from rest_framework import generics


# Create your views here.
class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSearializer
