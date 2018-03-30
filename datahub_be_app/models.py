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

class Propsales00(models.Model):
    id  = models.TextField(12,primary_key=True)
    meansp = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    minsp = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    maxsp = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    mediansp = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    totsp = models.DecimalField(max_digits=16,decimal_places=2,null=True)
    nums = models.DecimalField(max_digits=3,decimal_places=0,null=True)
    mhi = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    pir = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    mgr_phi = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    mmoc_phi = models.DecimalField(max_digits=5,decimal_places=2,null=True)

class Propsales17(models.Model):
    id  = models.TextField(12,primary_key=True)
    meansp = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    minsp = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    maxsp = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    mediansp = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    totsp = models.DecimalField(max_digits=16,decimal_places=2,null=True)
    nums = models.DecimalField(max_digits=4,decimal_places=0,null=True)
    mhi = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    pir = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    mgr_phi = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    mmoc_phi = models.DecimalField(max_digits=5,decimal_places=2,null=True)

class Singfamhouse(models.Model):
    id  = models.TextField(12,primary_key=True)
    mean_sfno = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    tot_sfno = models.DecimalField(max_digits=16,decimal_places=2,null=True)
    num_sfno = models.DecimalField(max_digits=3,decimal_places=0,null=True)
    mean_sfoo = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    tot_sfoo = models.DecimalField(max_digits=16,decimal_places=2,null=True)
    num_sfoo = models.DecimalField(max_digits=4,decimal_places=0,null=True)
    prc_sfno = models.DecimalField(max_digits=5,decimal_places=2,null=True)

class Singfamhouse00(models.Model):
    id  = models.TextField(12,primary_key=True)
    mean_sfno = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    tot_sfno = models.DecimalField(max_digits=16,decimal_places=2,null=True)
    num_sfno = models.DecimalField(max_digits=3,decimal_places=0,null=True)
    mean_sfoo = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    tot_sfoo = models.DecimalField(max_digits=16,decimal_places=2,null=True)
    num_sfoo = models.DecimalField(max_digits=4,decimal_places=0,null=True)
    prc_sfno = models.DecimalField(max_digits=5,decimal_places=2,null=True)

class Singfamhouse17(models.Model):
    id  = models.TextField(12,primary_key=True)
    mean_sfno = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    tot_sfno = models.DecimalField(max_digits=16,decimal_places=2,null=True)
    num_sfno = models.DecimalField(max_digits=3,decimal_places=0,null=True)
    mean_sfoo = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    tot_sfoo = models.DecimalField(max_digits=16,decimal_places=2,null=True)
    num_sfoo = models.DecimalField(max_digits=4,decimal_places=0,null=True)
    prc_sfno = models.DecimalField(max_digits=5,decimal_places=2,null=True)

class DECRace_Bgs_00(models.Model):
    id  = models.TextField(12,primary_key=True)
    pop_00 = models.DecimalField(max_digits=6,decimal_places=0,null=False)
    ptwhnl_00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptblknl_00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptnanl_00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptasnl_00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptpanl_00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptothnl_00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    pt2mnl_00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptlat_00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)

class CompassRace_Bgs_1314(models.Model):
    id  = models.TextField(12,primary_key=True)
    pop_13 = models.DecimalField(max_digits=6,decimal_places=0,null=False)
    pop_14 = models.DecimalField(max_digits=6,decimal_places=0,null=False)
    ptwhnl_13 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptwhnl_14 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptblknl_13 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptblknl_14 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptasnl_13 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptasnl_14 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptothnl_13 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptothnl_14 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptlat_13 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptlat_14 = models.DecimalField(max_digits=6,decimal_places=2,null=False)

class ACSRace_Bgs_16(models.Model):
    id  = models.TextField(12,primary_key=True)
    pop_16 = models.DecimalField(max_digits=6,decimal_places=0,null=False)
    ptwhnl_16 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptblknl_16 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptnanl_16 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptasnl_16 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptpanl_16 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptothnl_16 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    pt2mnl_16 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    ptlat_16 = models.DecimalField(max_digits=6,decimal_places=2,null=False)


