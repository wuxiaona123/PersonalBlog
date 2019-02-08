from django.conf.urls import url
from article.views import Home

urlpatterns = [
    url(r'^$', Home.as_view(), name='home')
]