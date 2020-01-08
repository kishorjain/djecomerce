from .models import Product_details
from rest_framework import serializers
 
class ProductSerializers(serializers.ModelSerializer):
   class Meta:
       model=Product_details
       fields=('id','productName','ProductDes','isbn','productCostPrice','productRetailPrice','create_ts')