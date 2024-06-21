from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    #my_discounts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            #'my_discounts',
        ]

    # def get_my_discounts(self, obj):
    #     return obj.get_discounts()

