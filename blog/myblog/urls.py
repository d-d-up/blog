# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import MyBlogListView, BlogContentCreateView, BlogContentDetailView
urlpatterns = [
    url(r'^$', MyBlogListView.as_view(), name='myblog_list'),
    url(r'^create/$', BlogContentCreateView.as_view(), name='myblog_create'),
    url(r'^detail/(?P<pk>[\d]+).html$', BlogContentDetailView.as_view(), name='myblog_detail'),

]
