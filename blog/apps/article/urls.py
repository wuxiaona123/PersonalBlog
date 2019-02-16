from django.conf.urls import url
from article.views import Home, Publish, Summernoteimg,Details,Post_commentView

urlpatterns = [
    # 首页
    url(r'^$', Home.as_view(), name='home'),
    # 发帖页面
    url(r'^publish/$', Publish.as_view(), name='publish'),
    # summernote编辑器上传图片
    url(r'^summernoteimg/$', Summernoteimg.as_view(), name='summernoteimg'),
    # 详情
    url(r'^details/(?P<id>\d+)$', Details.as_view(), name='details'),
    # 评论
    url(r'^comment/(?P<post_pk>[0-9]+)/$', Post_commentView.as_view(), name='文章评论'),

]
