# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ast import literal_eval

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.models import Product, Traveller, TravellerContactInfo
from products.serializers import ProductDetailSerializer, ProductSerializer, TravellerSerializer
# Create your views here.


class ProductList(APIView):
    """
    List all products, or create a new products.
    """
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """
    Retrieve & update a product.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductDetailSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookTicket(APIView):
    """
    List all booking, or create a new ticket booking.
    """

    def save_contact_info(self, information):
        info = literal_eval(information)

        title = info.get('title')
        name = info.get('name')
        ph_no = info.get('ph_no')
        email = info.get('email')

        contact_obj = TravellerContactInfo(title=title, name=name, ph_number=ph_no, email=email)
        contact_obj.save()
        return contact_obj

    def get(self, request):
        traveller = Traveller.objects.all()
        serializer = TravellerSerializer(traveller, many=True)
        return Response(serializer.data)

    def post(self, request):
        title = request.data.get('title')
        fname = request.data.get('first_name')
        lname = request.data.get('last_name', '')
        age = request.data.get('age')
        nationality = request.data.get('nationality', 'Indian')
        product = request.data.get('product')

        contact_info = request.data.get('contact')
        contact_obj = self.save_contact_info(contact_info)

        traveller = Traveller(title=title, first_name=fname, last_name=lname, age=age, nationality=nationality, product_id=product, contact_info=contact_obj)
        traveller.save()
        serializer = TravellerSerializer(traveller)
        return Response(serializer.data)
