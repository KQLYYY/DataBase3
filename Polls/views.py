from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import MySQLdb
from django.shortcuts import render, redirect
import csv
import random
import codecs
import json
import MySQLdb as mdb


def trr1(request):
    db = MySQLdb.connect(host="localhost" , user="root" , passwd="MySql12321" , db="mydb")
    cur = db.cursor()
    query = ''' CREATE TRIGGER `tr1` AFTER INSERT ON `mydb`.`order`
                        FOR EACH ROW INSERT INTO log (msg) VALUES("DIY");'''
    cur.execute(query)
    db.close()
    return redirect('/admin/Polls/')

def trr2(request):
    db = MySQLdb.connect(host="localhost" , user="root" , passwd="MySql12321" , db="mydb")
    cur = db.cursor()
    query = '''DROP TRIGGER IF EXISTS `tr1`;'''
    cur.execute(query)
    db.close()
    return redirect('/admin/Polls/')