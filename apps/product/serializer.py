from rest_framework import serializers
from apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','category','title','description','price','status','created_at','updated_at']


class GenerateDynamicSerializer(serializers.Serializer):
    product_size =serializers.IntegerField(min_value=1,max_value=100)
