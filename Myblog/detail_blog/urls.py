#-*-coding:utf-8-*-
from django.conf.urls import url
from django.urls import path , re_path
from . import views   #����Ӧ�õ���ͼ����
app_name = 'detail_blog'  #����app(����������ռ�)
urlpatterns = [
    path('', views.index,name = 'index'),    # �����һ����������ַ���ڶ�������ͼ�еĶ�Ӧ�������������Ǻ����ı���
    path('', views.index_1,name = 'index_1'),
    path('', views.index_2,name = 'index_2'),
    path('', views.index_3,name = 'index_3'),
    re_path('^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    re_path('^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'), #���°���ʱ�����ĺ���
    re_path(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'), #���°��������з���
    re_path(r'^tags/(?P<pk>[0-9]+)/$', views.tags, name='tags'),
]