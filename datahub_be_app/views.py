from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PropsalesSerializer, Propsales00Serializer, Propsales17Serializer, SingfamhouseSerializer, Singfamhouse00Serializer, Singfamhouse17Serializer
from .models import Propsales, Propsales00, Propsales17, Singfamhouse, Singfamhouse00, Singfamhouse17

def test_view(request):
    return render(request, 'test.html')

class PropsalesView(viewsets.ReadOnlyModelViewSet):
    queryset = Propsales.objects.all()
    serializer_class = PropsalesSerializer

class Propsales00View(viewsets.ReadOnlyModelViewSet):
    queryset = Propsales00.objects.all()
    serializer_class = Propsales00Serializer

class Propsales17View(viewsets.ReadOnlyModelViewSet):
    queryset = Propsales17.objects.all()
    serializer_class = Propsales17Serializer

class SingfamhouseView(viewsets.ReadOnlyModelViewSet):
    queryset = Singfamhouse.objects.all()
    serializer_class = SingfamhouseSerializer

class Singfamhouse00View(viewsets.ReadOnlyModelViewSet):
    queryset = Singfamhouse00.objects.all()
    serializer_class = Singfamhouse00Serializer

class Singfamhouse17View(viewsets.ReadOnlyModelViewSet):
    queryset = Singfamhouse17.objects.all()
    serializer_class = Singfamhouse17Serializer


