from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import HealthSerializer
from .models import Health


def test_view(request):
    return render(request, 'test.html')


class HealthView(viewsets.ModelViewSet):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
