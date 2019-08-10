#-*-coding:utf-8-*-
from django.shortcuts import render , get_object_or_404 # 这是获取数据时的方法
from .models import Post ,Category ,Tag
import markdown
from comments.form import CommentForm

from django.http import HttpResponse
# Create your views here.
def index(request): #  必须的参数request
    #return HttpResponse('Welcome to my new blog!')       #通过HttpResponse 来返回内容
    '''
    return render(request, 'detail_blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    })
    '''
    post_list = Post.objects.all().order_by('-create_time')   #model中创建的数据表的名称 - 是逆序的意思
    return render(request, 'detail_blog/index.html', context={
        'post_list': post_list
    })
def index_1(request):
    post_list = Post.objects.all()
    return render(request,'detail_blog/detail.html',context={
        'post_list': post_list
    })
def index_2(request):
    return render(request,'detail_blog/about.html')
def index_3(request):
    return render(request,'detail_blog/contact.html')
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 引入markdown 格式，让文档能够转化为HTML格式
    post.body = markdown.markdown(post.body,
                                  extensions=[    # 以下是对markdown语法的扩展
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'detail_blog/detail.html', context=context)   # 返回详情页的HTML页面
# 按照创建时间进行分类，这里选择数据是通过filter的过滤方法来实现
def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    ).order_by('-create_time')
    return render(request, 'detail_blog/index.html', context={'post_list': post_list})
# 按照内容类别进行分类，这里选择数据是通过filter的过滤方法来实现
def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'detail_blog/index.html', context={'post_list': post_list})
# 标签云的设置
def tags(request):
    tags_list = Tag.objects.all().order_by('-create_time')
    return render(request, 'detail_blog/index.html', context={'tags_list': tags_list})
