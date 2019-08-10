#-*-coding:utf-8-*-
from django.conf.urls import url
from django.urls import path , re_path
from . import views   #导入应用的视图函数
app_name = 'detail_blog'  #表明app(这叫做命名空间)
urlpatterns = [
    path('', views.index,name = 'index'),    # 这里第一个参数是网址，第二个是视图中的对应函数，第三个是函数的别名
    path('', views.index_1,name = 'index_1'),
    path('', views.index_2,name = 'index_2'),
    path('', views.index_3,name = 'index_3'),
    re_path('^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    re_path('^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'), #文章按照时间分类的函数
    re_path(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'), #文章按照类别进行分类
    re_path(r'^tags/(?P<pk>[0-9]+)/$', views.tags, name='tags'),
]