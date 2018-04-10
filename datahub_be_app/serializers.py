from rest_framework import serializers
from .models import Propsales,Propsales00,Propsales17,Singfamhouse,Singfamhouse00,Singfamhouse17,DECRace_Bgs_00,CompassRace_Bgs_1314,ACSRace_Bgs_16,LTDBACS_trts_7016

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


class LTDBACS_trts_7016Serializer (serializers.ModelSerializer):
    class Meta:
        model = LTDBACS_trts_7016
        fields = ('id','pop70','nhwht70','pnhwht70','nhblk70','pnhblk70','asian70','pasian70','haw70','phaw70','hu70','vac70','pvac70','ohu70','pohu70','own70','pown70','rent70','prent70','mhmval70a17','mhmval70','mrent70','mrent70a17','hinc70','hinc70a17','pop80','nhwht80','pnhwht80','nhblk80','pnhblk80','ntv80','pntv80','asian80','pasian80','hisp80','phisp80','haw80','phaw80','hu80','vac80','pvac80','ohu80','pohu80','own80','pown80','rent80','prent80','mhmval80','mhmval80a17','mrent80','mrent80a17','hinc80','hinc80a17','hincw80','hincw80a17','hincb80','hincb80a17','hinch80','hinch80a17','hinca80','hinca80a17','pop90','nhwht90','pnhwht90','nhblk90','pnhblk90','ntv90','pntv90','asian90','pasian90','hisp90','phisp90','haw90','phaw90','hu90','vac90','pvac90','ohu90','pohu90','own90','pown90','rent90','prent90','mhmval90','mhmval90a17','mrent90','mrent90a17','hinc90','hinc90a17','hincw90','hincw90a17','hincb90','hincb90a17','hinch90','hinch90a17','hinca90','hinca90a17','pop00','nhwht00','pnhwht00','nhblk00','pnhblk00','ntv00','pntv00','asian00','pasian00','hisp00','phisp00','haw00','phaw00','hu00','vac00','pvac00','ohu00','pohu00','own00','pown00','rent00','prent00','mhmval00','mhmval00a17','mrent00','mrent00a17','hinc00','hinc00a17','hincw00','hincw00a17','hincb00','hincb00a17','hinch00','hinch00a17','hinca00','hinca00a17','pop10','nhwht10','pnhwht10','nhblk10','pnhblk10','ntv10','pntv10','asian10','pasian10','hisp10','phisp10','haw10','phaw10','hu10','vac10','pvac10','ohu10','pohu10','own10','pown10','rent10','prent10','mhmval12','mhmval12a17','mrent12','mrent12a17','hinc12','hinc12a17','hincw12','hincw12a17','hincb12','hincb12a17','hinch12','hinch12a17','hinca12','hinca12a17','pop16','nhwht16','pnhwht16','nhblk16','pnhblk16','ntv16','pntv16','asian16','pasian16','haw16','phaw16','oth16','poth16','twomr16','ptwomr16','hisp16','phisp16','hu16','ohu16','pohu16','vac16','pvac16','own16','pown16','rent16','prent16','mhmval16','mrent16','mhmval16a17','mrent16a17','hinc16','hinc16a17','hincw16','hincw16a17','hincb16','hincb16a17','hincn16','hincn16a17','hinca16','hinca16a17','hincp16','hincp16a17','hinco16','hinco16a17','hincm16','hincm16a17','hinch16','hinch16a17')
