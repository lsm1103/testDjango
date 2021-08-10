import json, traceback
from django.views import View
from django.core import serializers
from django.shortcuts import render, HttpResponse
from author import models


# Create your views here.
class Author(View):
    def get(self,request):
        try:
            if not request.body:
                return HttpResponse(status=422, content=f"未输入参数")
            body = json.loads(request.body)
            print(f"post 方法, body:{body}")
            info = models.Author.objects.filter(name=body['name'])
        except Exception:
            return HttpResponse(status=400, content=f"失败, traceback:{traceback.print_exc()}")
        return HttpResponse(json.dumps([item.to_dict() for item in info ]) )

    def post(self,request):
        try:
            if not request.body:
                return HttpResponse(status=422, content=f"未输入参数")
            body = json.loads(request.body)
            print(f"post 方法, body:{body}")
            book = models.Author(**body)
            book.save()
        except Exception:
            return HttpResponse(status=400, content=f"失败, traceback:{traceback.print_exc()}")
        return HttpResponse(content='成功')

