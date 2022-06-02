from rest_framework import serializers
from .models import Category, Product

# class ProductModel():
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.price = validated_data.get("price", instance.price)
        instance.save()
        return instance