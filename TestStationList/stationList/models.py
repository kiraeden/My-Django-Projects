from django.db import models

class StationData(models.Model):
    pc_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    current_project = models.CharField(max_length=50)
    working = models.BooleanField()
    clapper = models.BooleanField()
    dac = models.BooleanField()
    pmd = models.BooleanField()
    maintenance = models.CharField(max_length=50)
    in_use_for = models.CharField(max_length=50)
    checked_out = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    sspec = models.CharField(max_length=10)
    
    def __str__(self):
        return pcName