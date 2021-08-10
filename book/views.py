import json, traceback
from django.views import View
from django.core import serializers
from django.shortcuts import render, HttpResponse
from book import models

# Create your views here.
class Book(View):
    def get(self,request):
        try:
            if not request.body:
                return HttpResponse(status=422, content=f"未输入参数")
            body = json.loads(request.body)
            print(f"get, body:{body}")
            info = models.Book.objects.filter(author=body['author'])
        except Exception:
            return HttpResponse(status=400, content=f"失败, traceback:{traceback.print_exc()}")
        return HttpResponse(json.dumps([item.to_dict() for item in info ]) )

    def post(self,request):
        try:
            if not request.body:
                return HttpResponse(status=422, content=f"未输入参数")
            body = json.loads(request.body)
            print(f"post, body:{body}")
            book = models.Book(**body)
            book.save()
        except Exception:
            return HttpResponse(status=400, content=f"失败, traceback:{traceback.print_exc()}")
        return HttpResponse(content='成功')


{
    "author": "大宝贝",
    "publish_date": "2021-08-09 15:24:12",
    "country": "为了考察您的技术能力与我们公司岗位的匹配性，麻烦您做一下下面的考试。"
}