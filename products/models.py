from django.db import models

# Create your models here.
class WareHouseA(models.Model):
    UID=models.CharField(max_length=20,primary_key=True)
    Product_Name=models.CharField(max_length=15,null=False)
    quantity=models.IntegerField(default=0, null=False)
    Time_In=models.DateTimeField(auto_now=True,null=False)
    # Time_Out=models.DateTimeField(auto_now=False,blank=True)
    destination=models.CharField(max_length=5)
    status=models.CharField(max_length=15,null=False,default="In Storage")


class WareHouseB(models.Model):
    UID=models.CharField(max_length=20,primary_key=True)
    Product_Name=models.CharField(max_length=15,null=False)
    quantity=models.IntegerField(default=0, null=False)
    Time_In=models.DateTimeField(auto_now=True,null=False)
    Time_Out=models.DateTimeField(auto_now=False)



class WareHouseC(models.Model):
    UID=models.CharField(max_length=20,primary_key=True)
    Product_Name=models.CharField(max_length=15,null=False)
    quantity=models.IntegerField(default=0, null=False)
    Time_In=models.DateTimeField(auto_now=True,null=False)
    Time_Out=models.DateTimeField(auto_now=False)
    