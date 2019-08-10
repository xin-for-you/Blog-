#-*-coding:utf-8-*- 
from django.urls import path , re_path
from . import views   #导入应用的视图函数
app_name = 'comments'  #表明app(这叫做命名空间)
urlpatterns = [
    re_path(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment,name = 'post_comment'),    # 这里第一个参数是网址，第二个是视图中的对应函数，第三个是函数的别名
]