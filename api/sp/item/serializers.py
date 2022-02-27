from rest_framework import serializers
from api.sp.item.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'category', 'subcategory', 'name', 'amount')
