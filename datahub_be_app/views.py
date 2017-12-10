from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_csv.parsers import CSVParser
from rest_framework_csv.renderers import CSVRenderer
from .serializers import HealthSerializer, PropsalesSerializer
from .models import Health, Propsales


def test_view(request):
    return render(request, 'test.html')


class HealthView(viewsets.ModelViewSet):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PropsalesView(viewsets.ModelViewSet):
    queryset = Propsales.objects.all()
    parser_classes = (CSVParser,) + tuple(api_settings.DEFAULT_PARSER_CLASSES)
    renderer_classes = (CSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    serializer_class = PropsalesSerializer
