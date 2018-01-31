#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
# Create your views here.
def index(request):
     return render(request,'booktest/index.html')

def myExp(request):
     print 'myExp'
     return HttpResponse('hello')

#上传图片
def uploadPic(request):
     return render(request,'booktest/uploadPic.html')


def uploadHandle(request):
     if request.method == 'POST':
          pic1= request.FILES['pic1']
          # fname = '%s/cars/%s'%(settings.MEDIA_ROOT,f1.name)
          picName = os.path.join(settings.MEDIA_ROOT,pic1.name)
          with open(picName,'w') as pic:
               for c in pic1.chunks():
                    pic.write(c)
          # return HttpResponse('OK')
          # return HttpResponse('<img src="/abc/media/%s"/>'%(pic1.name))
          return HttpResponse('<img src="%smedia/%s"/>'%(settings.STATIC_URL,pic1.name))
     else:
          return HttpResponse('Error')