# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50, default='3 hours')
    age_requirement = models.CharField(max_length=50, blank=True)
    medical_requirement = models.CharField(max_length=50, blank=True, default='')
    about_activity = models.CharField(max_length=50, blank=True, default='')
    about_vendor = models.CharField(max_length=50, blank=True, default='')
    summary = models.CharField(max_length=50, blank=True, default='')
    food = models.CharField(max_length=50, blank=True, default='')
    other_facilities = models.CharField(max_length=50, blank=True, default='')
    price = models.IntegerField()

    def __str__(self):
        return self.title


class TravellerContactInfo(models.Model):
    title = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    ph_no = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class TravellersInfo(models.Model):
    title = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    nationality = models.CharField(max_length=20, default='Indian')
    passport = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    travellers = models.ManyToManyField(TravellersInfo)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    contact_info = models.ForeignKey(TravellerContactInfo, on_delete=models.CASCADE)
