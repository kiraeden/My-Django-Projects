from django.db import models

class StationData(models.Model):
    pc_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    current_project = models.CharField(max_length=50)
    working = models.BooleanField()
    clapper = models.BooleanField()
    dac = models.BooleanField()
    pmd = models.BooleanField()
    maintenance = models.DateField(auto_now=False, auto_now_add=False, editable=True, blank=True, null=True)
    maintainer = models.CharField(max_length=50)
    in_use_for = models.CharField(max_length=50)
    checked_out = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    sspec = models.CharField(max_length=10)
    ip_address = models.GenericIPAddressField()
    pc_os = models.CharField(max_length=20)
    mac_address = models.CharField(max_length=100)
    box_id = models.CharField(max_length=100) #This is a future feature where we track associated fixture IDs separate from the pc_name
    pc_port_num = models.CharField(max_length=20)
    
    def __str__(self):
        return pc_name