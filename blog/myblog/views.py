# coding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import BlogSort, BlogContent
from .forms import BlogContentCreateForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy


class MyBlogListView(ListView):
    """博客内容列表"""
    model = BlogContent
    template_name = "myblog_list.html"
    paginate_by = 5
    context_object_name = 'blog_contents'

    def get_queryset(self):
        """重写."""
        blog_contents = BlogContent.objects.filter(sort__blog_type=0).order_by('-create_time')
        return blog_contents

    def get_context_data(self, **kwargs):
        """重写上下文函数，加入自己的内容."""
        context = super(MyBlogListView, self).get_context_data(**kwargs)
        sort_list = BlogSort.objects.filter(blog_type=0)
        content_four = BlogContent.objects.filter(sort__blog_type=0).order_by('-create_time')[0:4]
        content_all = BlogContent.objects.filter(sort__blog_type=0).order_by('-create_time')
        # print(content_all)
        # print(BlogContent.objects.filter())
        context['sort_list'] = sort_list
        context['content_four'] = content_four
        context['content_all'] = content_all
        return context


class BlogContentCreateView(LoginRequiredMixin, CreateView):
    """博客内容创建"""
    template_name = "myblog_create.html"
    form_class = BlogContentCreateForm
    success_url = reverse_lazy("myblog:myblog_list")


class BlogContentDetailView(DetailView):
    """博客内容详情"""
    model = BlogContent
    template_name = "myblog_detail.html"
    context_object_name = "blog_content"

    def get_object(self):
        """点击进来增加浏览次数"""
        object = super(BlogContentDetailView, self).get_object()
        # 修改属性值
        object.views = object.views + 1
        object.save()
        # Return the object
        return object

    def get_context_data(self, **kwargs):
        """重写上下文函数，加入自己的内容."""
        context = super(BlogContentDetailView, self).get_context_data(**kwargs)
        sort_list = BlogSort.objects.filter(blog_type=0)
        sort_id = self.object.sort_id
        content_four = BlogContent.objects.order_by('-create_time')[0:4]
        sort_content_four = BlogContent.objects.filter(Q(sort_id=sort_id), ~Q(pk=self.object.pk)).order_by('-create_time')[0:4]
        context['sort_list'] = sort_list
        context['content_four'] = content_four
        context['sort_content_four'] = sort_content_four
        return context


class BlogSortContentListView(ListView):
    """博客分类内容列表"""
    model = BlogSort
    template_name = "myblog_list.html"
    context_object_name = 'blog_contents'
    paginate_by = 5

    def get_queryset(self):
        """重写."""
        sort_id = self.kwargs.get('pk')

        blog_sort_objects = BlogContent.objects.all()
        if sort_id:
            blog_sort_objects = blog_sort_objects.filter(sort__id=sort_id)
        return blog_sort_objects.all()

    def get_context_data(self, **kwargs):
        """重写上下文函数，加入自己的内容."""
        context = super(BlogSortContentListView, self).get_context_data(**kwargs)
        sort_list = BlogSort.objects.filter(blog_type=0)
        content_four = BlogContent.objects.order_by('-create_time')[0:4]
        context['sort_list'] = sort_list
        context['content_four'] = content_four
        return context


class MyNovelListView(ListView):
    """小说内容列表"""
    model = BlogContent
    template_name = "mynovel_list.html"
    paginate_by = 5
    context_object_name = 'blog_contents'

    def get_queryset(self):
        """重写."""
        blog_contents = BlogContent.objects.filter(sort__blog_type=1).order_by('-create_time')
        return blog_contents

    def get_context_data(self, **kwargs):
        """重写上下文函数，加入自己的内容."""
        context = super(MyNovelListView, self).get_context_data(**kwargs)
        sort_list = BlogSort.objects.filter(blog_type=1)
        content_four = BlogContent.objects.filter(sort__blog_type=1).order_by('-create_time')[0:4]
        content_all = BlogContent.objects.filter(sort__blog_type=1).order_by('-create_time')
        # print(content_all)
        # print(BlogContent.objects.filter())
        context['sort_list'] = sort_list
        context['content_four'] = content_four
        context['content_all'] = content_all
        return context


class MySoupListView(ListView):
    """鸡汤内容列表"""
    model = BlogContent
    template_name = "mysoup_list.html"
    paginate_by = 5
    context_object_name = 'blog_contents'

    def get_queryset(self):
        """重写."""
        blog_contents = BlogContent.objects.filter(sort__blog_type=2).order_by('-create_time')
        return blog_contents

    def get_context_data(self, **kwargs):
        """重写上下文函数，加入自己的内容."""
        context = super(MySoupListView, self).get_context_data(**kwargs)
        sort_list = BlogSort.objects.filter(blog_type=2)
        content_four = BlogContent.objects.filter(sort__blog_type=2).order_by('-create_time')[0:4]
        content_all = BlogContent.objects.filter(sort__blog_type=2).order_by('-create_time')
        # print(content_all)
        # print(BlogContent.objects.filter())
        context['sort_list'] = sort_list
        context['content_four'] = content_four
        context['content_all'] = content_all
        return context


class MyRoadListView(ListView):
    """走过的路内容列表"""
    model = BlogContent
    template_name = "myroad_list.html"
    paginate_by = 5
    context_object_name = 'blog_contents'

    def get_queryset(self):
        """重写."""
        blog_contents = BlogContent.objects.filter(sort__blog_type=3).order_by('-create_time')
        return blog_contents

    def get_context_data(self, **kwargs):
        """重写上下文函数，加入自己的内容."""
        context = super(MyRoadListView, self).get_context_data(**kwargs)
        sort_list = BlogSort.objects.filter(blog_type=3)
        content_four = BlogContent.objects.filter(sort__blog_type=3).order_by('-create_time')[0:4]
        content_all = BlogContent.objects.filter(sort__blog_type=3).order_by('-create_time')
        # print(content_all)
        # print(BlogContent.objects.filter())
        context['sort_list'] = sort_list
        context['content_four'] = content_four
        context['content_all'] = content_all
        return context


class MyHeartListView(ListView):
    """少女心内容列表"""
    model = BlogContent
    template_name = "myheart_list.html"
    paginate_by = 5
    context_object_name = 'blog_contents'

    def get_queryset(self):
        """重写."""
        blog_contents = BlogContent.objects.filter(sort__blog_type=4).order_by('-create_time')
        return blog_contents

    def get_context_data(self, **kwargs):
        """重写上下文函数，加入自己的内容."""
        context = super(MyHeartListView, self).get_context_data(**kwargs)
        sort_list = BlogSort.objects.filter(blog_type=4)
        content_four = BlogContent.objects.filter(sort__blog_type=4).order_by('-create_time')[0:4]
        content_all = BlogContent.objects.filter(sort__blog_type=4).order_by('-create_time')
        # print(content_all)
        # print(BlogContent.objects.filter())
        context['sort_list'] = sort_list
        context['content_four'] = content_four
        context['content_all'] = content_all
        return context
