#-*-coding:utf-8-*- 
from django.urls import path , re_path
from . import views   #����Ӧ�õ���ͼ����
app_name = 'comments'  #����app(����������ռ�)
urlpatterns = [
    re_path(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment,name = 'post_comment'),    # �����һ����������ַ���ڶ�������ͼ�еĶ�Ӧ�������������Ǻ����ı���
]