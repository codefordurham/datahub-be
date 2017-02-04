from django.db import models


class Health(models.Model):
    status = models.CharField(max_length=25)
