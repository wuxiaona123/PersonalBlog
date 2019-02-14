import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

# 生成随机验证码
from db.app_common import set_password
from user.forms import RegisterForms, LoginForms
from user.models import UserModels


def setcode(request):
    # 生成随机验证码
    code = "".join([str(random.randint(0, 9)) for _ in range(4)])
    # 把验证码保存到ssesion
    request.session['verification'] = code
    return code


# 登录
class Login(View):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        data = request.POST
        form = LoginForms(data)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            request.session['id'] = user.pk
            request.session['nickname'] = user.nickname
            return redirect('article:home')
        else:
            context = {
                'form': form,
            }
            return render(request, 'user/login.html', context=context)


# 注册
class Register(View):
    def get(self, request):
        code = setcode(request)
        return render(request, 'user/register.html', context={'code': code})

    def post(self, request):
        data = request.POST.dict()
        # 把验证码传过去验证。
        verification = request.session.get('verification', '')
        data['verification'] = verification
        form = RegisterForms(data)
        if form.is_valid():
            # 验证成功，存数据。
            cleane_data = form.cleaned_data
            password = set_password(cleane_data['password'])
            nickname = cleane_data['nickname']
            email = cleane_data['email']
            UserModels.objects.create(nickname=nickname, password=password, email=email)
            return redirect('user:login')
        else:
            code = setcode(request)
            context = {
                'form': form,
                'code': code,
            }
            return render(request, 'user/register.html', context=context)
