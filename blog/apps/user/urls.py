from django.conf.urls import url

from user.views import Login, Register

urlpatterns = [
    url(r'^login/$', Login.as_view(), name='login'),  # 登录
    url(r'^register/$', Register.as_view(), name='register'),  # 注册
]
