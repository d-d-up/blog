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

    def get_context_data(self, **kwargs):
        """重写上下文函数，加入自己的内容."""
        context = super(MyBlogListView, self).get_context_data(**kwargs)
        sort_list = BlogSort.objects.order_by('-create_time')
        content_four = BlogContent.objects.order_by('-create_time')[0:4]
        context['sort_list'] = sort_list
        context['content_four'] = content_four
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

    def get_context_data(self, **kwargs):
        """重写上下文函数，加入自己的内容."""
        context = super(BlogContentDetailView, self).get_context_data(**kwargs)
        sort_list = BlogSort.objects.all()
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
            blog_sort_objects = blog_sort_objects.filter(sort_id=sort_id)
        return blog_sort_objects.all()

    def get_context_data(self, **kwargs):
        """重写上下文函数，加入自己的内容."""
        context = super(BlogSortContentListView, self).get_context_data(**kwargs)
        sort_list = BlogSort.objects.all()
        content_four = BlogContent.objects.order_by('-create_time')[0:4]
        context['sort_list'] = sort_list
        context['content_four'] = content_four
        return context
