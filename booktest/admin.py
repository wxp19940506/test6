#coding=utf-8
from django.contrib import admin
from models import *
# Register your models here.

@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']

# admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
admin.site.register(UserInfo)