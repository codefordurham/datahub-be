from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PropsalesSerializer,Propsales00Serializer,Propsales17Serializer,SingfamhouseSerializer,Singfamhouse00Serializer,Singfamhouse17Serializer,DECRace_Bgs_00Serializer,CompassRace_Bgs_1314Serializer,ACSRace_Bgs_16Serializer,LTDBACS_trts_7016Serializer
from .models import Propsales,Propsales00,Propsales17,Singfamhouse,Singfamhouse00,Singfamhouse17,DECRace_Bgs_00,        CompassRace_Bgs_1314,ACSRace_Bgs_16,LTDBACS_trts_7016

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

class DECRace_Bgs_00View(viewsets.ReadOnlyModelViewSet):
    queryset = DECRace_Bgs_00.objects.all()
    serializer_class = DECRace_Bgs_00Serializer

class CompassRace_Bgs_1314View(viewsets.ReadOnlyModelViewSet):
    queryset = CompassRace_Bgs_1314.objects.all()
    serializer_class = CompassRace_Bgs_1314Serializer

class ACSRace_Bgs_16View(viewsets.ReadOnlyModelViewSet):
    queryset = ACSRace_Bgs_16.objects.all()
    serializer_class = ACSRace_Bgs_16Serializer

class LTDBACS_trts_7016View(viewsets.ReadOnlyModelViewSet):
    queryset = LTDBACS_trts_7016.objects.all()
    serializer_class = LTDBACS_trts_7016Serializer
