from rest_framework import serializers
from products.models import Product, Traveller, TravellerContactInfo


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'duration', 'age_requirement', 'medical_requirement',
                  'about_activity', 'about_vendor', 'summary', 'food', 'other_facilities', 'price')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'summary', 'price')


class TravellerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravellerContactInfo
        fields = ('name', 'email', 'ph_number')


class TravellerSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    contact_info = TravellerContactSerializer(read_only=True)

    class Meta:
        model = Traveller
        fields = ('id', 'title', 'first_name', 'last_name', 'age', 'nationality', 'product', 'contact_info')
