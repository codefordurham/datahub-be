from rest_framework import serializers
from .models import Health


class HealthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Health
        fields = ['id', 'status', 'url']
