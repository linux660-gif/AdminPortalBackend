from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import InvestorsProfile
from .serializer import InvestorSerializer

class InvestorViewSet(viewsets.ModelViewSet):
    queryset = InvestorsProfile.objects.all()
    serializer_class = InvestorSerializer
    