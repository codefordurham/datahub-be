from django.db import models

class Propsales(models.Model):
    id  = models.TextField(12,primary_key=True)
    meansp = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    minsp = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    maxsp = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    mediansp = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    totsp = models.DecimalField(max_digits=16,decimal_places=2,null=True)
    nums = models.DecimalField(max_digits=3,decimal_places=0,null=True)
    mhi = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    pir = models.DecimalField(max_digits=5,decimal_places=2,null=True)

class Singfamhouse(models.Model):
    id  = models.TextField(12,primary_key=True)
    mean_sfno = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    tot_sfno = models.DecimalField(max_digits=16,decimal_places=2,null=True)
    num_sfno = models.DecimalField(max_digits=3,decimal_places=0,null=True)
    mean_sfoo = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    tot_sfoo = models.DecimalField(max_digits=16,decimal_places=2,null=True)
    num_sfoo = models.DecimalField(max_digits=4,decimal_places=0,null=True)
    prc_sfno = models.DecimalField(max_digits=5,decimal_places=2,null=True)
