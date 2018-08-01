# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import MyBlogListView, BlogContentCreateView, BlogContentDetailView
from .forms import LoginForm
urlpatterns = [
    url(r'^$', MyBlogListView.as_view(), name='myblog_list'),
    url(r'^create/$', BlogContentCreateView.as_view(), name='myblog_create'),
    url(r'^detail/(?P<pk>[\d]+).html$', BlogContentDetailView.as_view(), name='myblog_detail'),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='blog_login'),
]
