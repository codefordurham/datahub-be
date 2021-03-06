from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import LTDBACS_trts_7016Serializer,bgs9800Serializer,bgs1318Serializer,durhamhdsSerializer, muniboundariesSerializer, cntyboundariesSerializer
from .models import LTDBACS_trts_7016,bgs9800,bgs1318,durhamhds,muniboundaries,cntyboundaries

def test_view(request):
    return render(request, 'test.html')

class LTDBACS_trts_7016View(viewsets.ReadOnlyModelViewSet):
    queryset = LTDBACS_trts_7016.objects.all()
    serializer_class = LTDBACS_trts_7016Serializer

class bgs9800View(viewsets.ReadOnlyModelViewSet):
    queryset = bgs9800.objects.all()
    serializer_class = bgs9800Serializer

class bgs1318View(viewsets.ReadOnlyModelViewSet):
    queryset = bgs1318.objects.all()
    serializer_class = bgs1318Serializer

class durhamhdsView(viewsets.ReadOnlyModelViewSet):
    queryset = durhamhds.objects.all()
    serializer_class = durhamhdsSerializer

class muniboundariesView(viewsets.ReadOnlyModelViewSet):
    queryset = muniboundaries.objects.all()
    serializer_class = muniboundariesSerializer

class cntyboundariesView(viewsets.ReadOnlyModelViewSet):
    queryset = cntyboundaries.objects.all()
    serializer_class = cntyboundariesSerializer
