# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
# from tinymce.models import HTMLField


class BlogSort(models.Model):
    """博客分类表"""
    name = models.CharField("分类名称", max_length=100)
    description = models.TextField("分类描述", blank=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, null=True)  # 创建时间
    update_time = models.DateTimeField("更新时间", auto_now=True, null=True)  # 更新时间
    blog_type = models.CharField('类型', max_length=2, default=0)  # 博客类型,0:技术篇,1：其他类型文章

    class Meta:
        """Custom attribute fields."""
        ordering = ['-create_time']
        db_table = 'bl_blog_sort'
        verbose_name = '博客分类表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class BlogContent(models.Model):
    """博客文章表"""
    sort = models.ForeignKey(BlogSort, related_name='BlogSort', null=True)  # 文章分类
    title = models.CharField("文章标题", max_length=100)
    content = models.TextField("文章内容", blank=True)
    # content = HTMLField("文章内容", blank=True)
    # image = models.ImageField(upload_to='blog', verbose_name='图片')
    create_time = models.DateTimeField("创建时间", auto_now_add=True, null=True)  # 创建时间
    update_time = models.DateTimeField("更新时间", auto_now=True, null=True)  # 更新时间

    class Meta:
        """Custom attribute fields."""
        ordering = ['-create_time']
        db_table = 'bl_blog_content'
        verbose_name = '博客文章表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

