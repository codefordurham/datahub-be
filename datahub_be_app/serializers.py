from rest_framework import serializers
from .models import Propsales, Singfamhouse

class PropsalesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Propsales
        fields = ('id', 'meansp', 'minsp','maxsp','mediansp','totsp','nums','mhi','pir')

class SingfamhouseSerializer (serializers.ModelSerializer):
    class Meta:
        model = Singfamhouse
        fields = ('id','mean_sfno','tot_sfno','num_sfno','mean_sfoo','tot_sfoo','num_sfoo','prc_sfno')
