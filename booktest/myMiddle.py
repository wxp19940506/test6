#coding=utf-8
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object
from django.shortcuts import HttpResponse

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print("中间件1请求")
        return None
    def process_response(self,request,response):
        print("中间件1返回")
        return response

class Row2(MiddlewareMixin):
    def process_request(self,request):
        print("中间件2请求")
        # return HttpResponse("走")
    def process_response(self,request,response):
        print("中间件2返回")
        return response

class Row3(MiddlewareMixin):
    def process_request(self,request):
        print("中间件3请求")
    def process_response(self,request,response):
        print("中间件3返回")
        return response