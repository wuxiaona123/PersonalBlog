from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self,requset):
        return render(requset,'article/index.html')
    def post(self,requset):
        return HttpResponse('主页！post')