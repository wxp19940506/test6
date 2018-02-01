#coding=utf-8

# Create your models here.
from django.db import models
# Register your models here.
class UserInfo(models.Model):
     uname = models.CharField(max_length=10)
     upwd = models.CharField(max_length=40)
     isDelete = models.BooleanField()

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField()
    bcommet = models.IntegerField()
    isDelete = models.BooleanField()


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField()
    book = models.ForeignKey('BookInfo',db_column='hbook_id')
