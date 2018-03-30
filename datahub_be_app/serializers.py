from rest_framework import serializers
from .models import Propsales,Propsales00,Propsales17,Singfamhouse,Singfamhouse00,Singfamhouse17,DECRace_Bgs_00,CompassRace_Bgs_1314,ACSRace_Bgs_16

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

class DECRace_Bgs_00Serializer (serializers.ModelSerializer):
    class Meta:
        model = DECRace_Bgs_00
        fields = ('id','pop_00','ptwhnl_00','ptblknl_00','ptnanl_00','ptasnl_00','ptpanl_00','ptothnl_00','pt2mnl_00','ptlat_00')

class CompassRace_Bgs_1314Serializer (serializers.ModelSerializer):
    class Meta:
        model = CompassRace_Bgs_1314
        fields = ('id','pop_13','pop_14','ptwhnl_13','ptwhnl_14','ptblknl_13','ptblknl_14','ptasnl_13','ptasnl_14','ptothnl_13','ptothnl_14','ptlat_13','ptlat_14')

class ACSRace_Bgs_16Serializer (serializers.ModelSerializer):
    class Meta:
        model = ACSRace_Bgs_16
        fields = ('id','pop_16','ptwhnl_16','ptblknl_16','ptnanl_16','ptasnl_16','ptpanl_16','ptothnl_16','pt2mnl_16','ptlat_16')

