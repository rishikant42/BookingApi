from rest_framework import serializers
from products.models import Product, Ticket, TravellerContactInfo, TravellersInfo


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
        fields = ('title', 'name', 'email', 'ph_no')


class TravellersInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravellersInfo
        fields = ('title', 'name', 'age', 'nationality', 'passport')


class TicketSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    contact_info = TravellerContactSerializer(read_only=True)
    travellers = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ('id', 'product', 'contact_info', 'travellers')

    def get_travellers(self, obj):
        travellers = obj.travellers.all()
        serializer = TravellersInfoSerializer(travellers, many=True)
        return serializer.data

