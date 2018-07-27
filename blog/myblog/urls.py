# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import MyBlogListView
urlpatterns = [
    url(r'^$', MyBlogListView.as_view(), name='myblog_list'),
]
