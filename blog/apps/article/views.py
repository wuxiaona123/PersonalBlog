from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from article.forms import SummernoteForm
from article.models import TagModels, ArticleModels
from user.models import UserModels
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# 首页
class Home(View):
    def get(self, request):
        # 是什么类型的标签
        tag = ['python', '前端', 'JAVA', 'php', 'NET', '数据库', '测试', 'C++']
        tagname = int(request.GET.get('tagname', -1))
        if tagname == -1:
            article = ArticleModels.objects.filter(is_delete=False)
        elif tag[tagname]:
            # 把指定标签下的帖子放入article
            article = []
            parenttag = TagModels.objects.get(tagname=tag[tagname], is_delete=False)
            childrentag = TagModels.objects.filter(parent=parenttag, is_delete=False)
            artiparent = ArticleModels.objects.filter(tagid=parenttag, is_delete=False)
            if artiparent.exists():
                article.append(artiparent[0])
            for i in childrentag:
                artichild = ArticleModels.objects.filter(tagid=i, is_delete=False)
                article = article + list(artichild)
        else:
            return HttpResponse('没有此标签')

        # Paginator 实现分页
        paginator = Paginator(article, 6)
        # 获取当前页面的页码
        page = request.GET.get('page', 1)

        # 获取对应页码的数据
        try:
            itemss = paginator.page(page)
        except PageNotAnInteger:
            # 页码不是整数，（是小数或字母） 显示第一页
            itemss = paginator.page(1)
        except EmptyPage:
            # 页码为超出范围 显示最后一页
            itemss = paginator.page(paginator.num_pages)
            # 合成响应    准备数据渲染页面

        context = {
            # 贴子数据
            "article": itemss,
            # 主标签下标
            "tagindex": tagname,
            # 标签名字
            "tagname": tag[tagname],
        }
        return render(request, 'article/index.html', context=context)


# 发帖
class Publish(View):
    def get(self, request):
        tag = TagModels.objects.filter()
        islogin = request.session.get('nickname', '')
        context = {
            'tag': tag,
            'islogin': islogin,
        }
        return render(request, 'article/publish.html', context=context)

    def post(self, request):
        userid = request.session.get('id', '')
        data = request.POST
        form = SummernoteForm(data)
        if form.is_valid():
            # 如果用户不存在
            try:
                user = UserModels.objects.get(pk=userid)
            except:
                tag = TagModels.objects.filter()
                islogin = request.session.get('nickname', '')
                context = {
                    'tag': tag,
                    'islogin': islogin,
                    'msg': '用户不存在'
                }
                return render(request, 'article/publish.html', context=context)
            cleane_data = form.cleaned_data
            tagid = cleane_data['tagid']
            # 处理如果tagdata不存在
            try:
                tagdata = TagModels.objects.get(pk=tagid)
            except:
                context = {
                    'form': form,
                    'msg': '没有所属标签',
                }
                return render(request, 'article/publish.html', context=context)
            articletitle = cleane_data['articletitle']
            editordata = cleane_data['editordata']
            ArticleModels.objects.create(articletitle=articletitle, tagid=tagdata, author=user,
                                         articlecontent=editordata)

            # 保存数据完了应该跳到详情页面，但是现在还没有详情页，先跳到本页面
            tag = TagModels.objects.filter()
            islogin = request.session.get('nickname', '')
            context = {
                'tag': tag,
                'islogin': islogin,
            }
            return render(request, 'article/publish.html', context=context)
        else:
            context = {
                'form': form,
            }
            return render(request, 'article/publish.html', context=context)


# Summernote富文本上传图片
class Summernoteimg(View):
    def get(self, request):
        return HttpResponse('发帖！get')

    def post(self, request):
        request = request.POST
        return JsonResponse({'fatie': 'post'})


# 详情
class Details(View):
    def get(self, request):
        return render(request, 'article/details.html')
