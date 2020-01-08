from django.db import models

# Create your models here.
class Product_details (models.Model):
   productName=models.CharField(max_length=200)
   ProductDes=models.CharField(max_length=500)
   productCostPrice=models.CharField(max_length=500,default=0)
   productRetailPrice=models.CharField(max_length=500,default=0)
   isbn=models.CharField(max_length=500,default=0)
   create_ts=models.DateTimeField(auto_now=True)
