from django.db import models

class NGO(models.Model):
    name = models.CharField(max_length=100)
    location = models.JSONField()

class Donor(models.Model):
    name = models.CharField(max_length=100)
    location = models.JSONField()
    matched_ngo = models.ForeignKey(NGO, on_delete=models.SET_NULL, null=True)
