# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ast import literal_eval

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.models import Product, Ticket, TravellerContactInfo
from products.serializers import ProductDetailSerializer, ProductSerializer, TicketSerializer, TravellerContactSerializer, TravellersInfoSerializer
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
        data = literal_eval(information)
        serializer = TravellerContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.instance

    def save_travellers_info(self, information):
        data = literal_eval(information)
        serializer = TravellersInfoSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.instance

    def get(self, request):
        traveller = Ticket.objects.all()
        serializer = TicketSerializer(traveller, many=True)
        return Response(serializer.data)

    def post(self, request):
        product = request.data.get('product')

        travellers_info = request.data.get('travellers')
        travellers_obj = self.save_travellers_info(travellers_info)

        contact_info = request.data.get('contact')
        contact_obj = self.save_contact_info(contact_info)

        ticket = Ticket(product_id=product, contact_info=contact_obj)
        ticket.save()
        for traveller in travellers_obj:
            ticket.travellers.add(traveller)

        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
