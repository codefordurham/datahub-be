from rest_framework import serializers
from .models import Health, Propsales

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = ['id', 'status', 'url']

class PropsalesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Propsales
        fields = ('id', 'meansp', 'minsp','maxsp','mediansp','totsp','nums','mhi','pir')
