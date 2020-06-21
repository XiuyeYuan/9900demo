"""
创建学生信息表模型
"""
from django.db import models


class User(models.Model):
    # userid
    UserId = models.IntegerField('UserId', primary_key=True)
    # password
    Password = models.CharField('Password', null=False, max_length=15)
    # createtime set the time
    CreateTime = models.DateTimeField(auto_now=True)

    # if not set,the name will be 'database_tablename'
    class Meta:
        db_table = 'User'


class Book(models.Model):
    # table book attributes
    BkId = models.IntegerField('Bkid', primary_key=True)
    BkTitle = models.CharField('BkTitle', max_length=15)
    BkAuthor = models.CharField('BkAuthor', max_length=15)
    BkPublisher = models.CharField('BkPublisher', max_length=15)
    BkPubDate = models.CharField('BkPubDate', max_length=8)
    Category = models.CharField('Category', max_length=15)
    Rating = models.CharField('Rating', null=True, max_length=15)
    ReviewNum = models.IntegerField('ReviewField', null=True)

    class Meta:
        db_table = 'Book'

#
# """
# 学生社团信息表
# """
# class studentUnion(models.Model):
#     # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
#     id = models.IntegerField(primary_key=True)
#     # 社团名称
#     unionName = models.CharField('社团名称', max_length=20)
#     # 社团人数
#     unionNum = models.IntegerField('人数', default=0)
#     # 社团负责人 关联Student的主键 即studentNum学号 一对一的关系,on__delete 属性在django2.0之后为必填属性后面会介绍
#     unionRoot = models.OneToOneField(Student, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'student_union'
#
#
# """
# OneToOneField： 一对一
# ForeignKey: 一对多
# ManyToManyField： 多对多(没有ondelete 属性)
# """
