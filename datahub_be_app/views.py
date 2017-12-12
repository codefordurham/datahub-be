from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PropsalesSerializer, SingfamhouseSerializer
from .models import Propsales, Singfamhouse

def test_view(request):
    return render(request, 'test.html')

class PropsalesView(viewsets.ReadOnlyModelViewSet):
    queryset = Propsales.objects.all()
    serializer_class = PropsalesSerializer

class SingfamhouseView(viewsets.ReadOnlyModelViewSet):
    queryset = Singfamhouse.objects.all()
    serializer_class = SingfamhouseSerializer

