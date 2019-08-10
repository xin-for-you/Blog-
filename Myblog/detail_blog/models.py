#-*-coding:utf-8-*-
#中文注释需要添加utf-8编码
'''
会通过两个语句将以下代码转化为数据库（这里使用的是django自带的数据库 SQlite3）创建对象的操作
python manage.py makemigrations 和 python manage.py migrate
都需要执行，
以下代码  python manage.py sqlmigrate detail_blog 0001 来查看对应的数据库语句   ———— 这就是django 的ORM工作机制
CREATE TABLE "detail_blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(60) NOT NULL, "body" text NOT NULL, "creat_time" datetime NOT NULL, "modify_time" datetime NOT NULL, "abstract" varchar(200) NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "category_id" integer NOT NULL REFERENCES "detail_blog_category" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "detail_blog_post_tags" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "post_id" integer NOT NULL REFERENCES "detail_blog_post" ("id") DEFERRABLE INITIALLY DEFERRED, "tag_id" integer NOT NULL REFERENCES "detail_blog_tag" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "detail_blog_post_author_id_67aa227f" ON "detail_blog_post" ("author_id");
CREATE INDEX "detail_blog_post_category_id_3031b74d" ON "detail_blog_post" ("category_id");
CREATE UNIQUE INDEX "detail_blog_post_tags_post_id_tag_id_ad6c95af_uniq" ON "detail_blog_post_tags" ("post_id", "tag_id");
CREATE INDEX "detail_blog_post_tags_post_id_40651e5a" ON "detail_blog_post_tags" ("post_id");
CREATE INDEX "detail_blog_post_tags_tag_id_b5a6f21d" ON "detail_blog_post_tags" ("tag_id");
COMMIT;
'''
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User     #最后的author属性的来源
       # 专门用于处理网站用户的注册、登录等流程 的内置模块

# Create your models here.
class Category(models.Model):  #定义类的时候一定要继承models.Model类
    '''
    Category 就是一个标准的 Python 类，它继承了 models.Model 类，类名为 Category
    Category 类有一个属性 name，它是 models.CharField 的一个实例。
    在数据库里创建一个名为 category 的表格，这个表格的一个列名为 name。
    还有一个列 id，Django 则会自动创建。
    '''
    name = models.CharField(max_length=100)   # charField 是定义字符型，最大长度是100
    def __str__(self):
        return self.name
class Tag(models.Model):
    # 定义一个标签
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Post(models.Model):
    #定义数据库的表,ORM会把python 的语句转换为数据库的执行代码
    title = models.CharField(max_length=60)
    body = models.TextField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    abstract = models.CharField(max_length=200,blank=True)
    #分类和标签 均为类的实例化
    #使用foreignkey时应该增加一个属性on_delete
    category = models.ForeignKey(Category,on_delete=models.CASCADE)      #  ForeignKey 表示一对多的关系
    tags = models.ManyToManyField(Tag,blank=True) #  ManyToManyField 表示多对多的关系
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('detail_blog:detail', kwargs={'pk': self.pk})  # 意思就是调用详情页时，反回怎样的url

    class Meta:
        ordering = ['-create_time','title','author']
