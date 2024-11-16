from django.db import models

# Create your models here.

class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'UserRegistrations'

class AssetLayerModel(models.Model):
    unithead = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    shift = models.IntegerField()
    productquantity = models.IntegerField()
    noofworkers = models.IntegerField()
    cdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
    class Meta:
        db_table = "AssetTable"

class UserIntegrationLayerModel(models.Model):
    engtool = models.CharField(max_length=100)
    filesize = models.FloatField()
    databasetype = models.CharField(max_length=10)
    humanmachineinterface = models.IntegerField()
    plcslaves = models.IntegerField()
    cdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
    class Meta:
        db_table = "IntegrationTable"

class UserCommunicationLayerModel(models.Model):
    protocol = models.CharField(max_length=100)
    transferred = models.CharField(max_length=100)
    filesize = models.FloatField()
    cdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
    class Meta:
        db_table = "CommunicationTable"


class UserInformationLayerModel(models.Model):
    metadata = models.CharField(max_length=100)
    storagesystems = models.CharField(max_length=100)
    schemaregistry = models.CharField(max_length=100)
    da = models.CharField(max_length=100)
    cdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
    class Meta:
        db_table = "InformationTable"

class UserFunctionalLayerModel(models.Model):
    productionmodel = models.CharField(max_length=100)
    modelbuilding = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    cdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
    class Meta:
        db_table = "FunctionalTable"

class UserBusinessLayerModel(models.Model):
    anomalyname = models.CharField(max_length=100)
    energyoptimization = models.CharField(max_length=100)
    conditionmonitor = models.CharField(max_length=100)
    cdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
    class Meta:
        db_table = "BusinessTable"