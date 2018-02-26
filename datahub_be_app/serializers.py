from rest_framework import serializers
from .models import Propsales, Propsales00, Propsales17, Singfamhouse, Singfamhouse00, Singfamhouse17

class PropsalesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Propsales
        fields = ('id', 'meansp', 'minsp','maxsp','mediansp','totsp','nums','mhi','pir')

class Propsales00Serializer (serializers.ModelSerializer):
    class Meta:
        model = Propsales00
        fields = ('id', 'meansp', 'minsp','maxsp','mediansp','totsp','nums','mhi','pir','mgr_phi','mmoc_phi')

class Propsales17Serializer (serializers.ModelSerializer):
    class Meta:
        model = Propsales17
        fields = ('id', 'meansp', 'minsp','maxsp','mediansp','totsp','nums','mhi','pir','mgr_phi','mmoc_phi')

class SingfamhouseSerializer (serializers.ModelSerializer):
    class Meta:
        model = Singfamhouse
        fields = ('id','mean_sfno','tot_sfno','num_sfno','mean_sfoo','tot_sfoo','num_sfoo','prc_sfno')

class Singfamhouse00Serializer (serializers.ModelSerializer):
    class Meta:
        model = Singfamhouse00
        fields = ('id','mean_sfno','tot_sfno','num_sfno','mean_sfoo','tot_sfoo','num_sfoo','prc_sfno')

class Singfamhouse17Serializer (serializers.ModelSerializer):
    class Meta:
        model = Singfamhouse17
        fields = ('id','mean_sfno','tot_sfno','num_sfno','mean_sfoo','tot_sfoo','num_sfoo','prc_sfno')

