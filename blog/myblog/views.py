# coding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BlogSort, BlogContent
from .forms import BlogContentCreateForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy


class MyBlogListView(ListView):
    """博客内容列表"""
    model = BlogContent
    template_name = "myblog_list.html"
    paginate_by = 1
    context_object_name = 'blog_contents'


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


