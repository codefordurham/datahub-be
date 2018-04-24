from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import LTDBACS_trts_7016Serializer,bgs00Serializer,bgs1317Serializer
from .models import LTDBACS_trts_7016,bgs00,bgs1317

def test_view(request):
    return render(request, 'test.html')

class LTDBACS_trts_7016View(viewsets.ReadOnlyModelViewSet):
    queryset = LTDBACS_trts_7016.objects.all()
    serializer_class = LTDBACS_trts_7016Serializer

class bgs00View(viewsets.ReadOnlyModelViewSet):
    queryset = bgs00.objects.all()
    serializer_class = bgs00Serializer

class bgs1317View(viewsets.ReadOnlyModelViewSet):
    queryset = bgs1317.objects.all()
    serializer_class = bgs1317Serializer

