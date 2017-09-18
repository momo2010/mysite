from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

class RegionInfo(models.Model):
    rid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=64)
    hostIP = models.CharField(max_length=32)
    regionName = models.CharField(max_length=32)
    licenseID = models.CharField(max_length=32)
    license = models.CharField(max_length=64)
    hostID = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    userphone = models.CharField(max_length=32)
    unitcode = models.CharField(max_length=32)
    unitname = models.CharField(max_length=64)
