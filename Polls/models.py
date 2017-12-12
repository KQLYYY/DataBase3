# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone



class Product(models.Model):
    idproduct = models.IntegerField(db_column='idProduct', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=45)  # Field name made lowercase.
    manufacturercountry = models.CharField(db_column='ManufacturerCountry', max_length=45)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=45)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45)  # Field name made lowercase.
    capacity = models.CharField(db_column='Capacity', max_length=45)  # Field name made lowercase.
    price = models.CharField(db_column='Price', max_length=45)  # Field name made lowercase.
    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'product'

class Client(models.Model):
    idclient = models.IntegerField(db_column='idClient', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='Fname', max_length=45)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=45)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', max_length=45)  # Field name made lowercase.
    def __str__(self):
        return self.fname

    class Meta:
        managed = False
        db_table = 'client'

class Store(models.Model):
    idstore = models.IntegerField(db_column='idStore', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.
    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'store'

class Order(models.Model):
    idorder = models.IntegerField(db_column='idOrder', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=45)  # Field name made lowercase.
    cost = models.CharField(db_column='Cost', max_length=45)  # Field name made lowercase.
    product_idproduct = models.ForeignKey(Product, models.DO_NOTHING, db_column='Product_idProduct')  # Field name made lowercase.
    store_idstore = models.ForeignKey(Store, models.DO_NOTHING, db_column='Store_idStore')  # Field name made lowercase.
    client_idclient = models.ForeignKey(Client, models.DO_NOTHING, db_column='Client_idClient')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'

class Log(models.Model):
    msg = models.CharField(max_length=45)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log'