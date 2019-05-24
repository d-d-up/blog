# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import MyBlogListView, MyNovelListView, MySoupListView, MyRoadListView, MyHeartListView, BlogContentCreateView, BlogContentDetailView, BlogSortContentListView
from .forms import LoginForm

urlpatterns = [
    url(r'^$', MyBlogListView.as_view(), name='myblog_list'),
    url(r'^admin/', admin.site.urls),
    url(r'^novel/$', MyNovelListView.as_view(), name='mynovel_list'),
    url(r'^soup/$', MySoupListView.as_view(), name='mysoup_list'),
    url(r'^road/$', MyRoadListView.as_view(), name='myroad_list'),
    url(r'^heart/$', MyHeartListView.as_view(), name='myheart_list'),
    url(r'^create/$', BlogContentCreateView.as_view(), name='myblog_create'),
    url(r'^detail/(?P<pk>[\d]+).html$', BlogContentDetailView.as_view(), name='myblog_detail'),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='blog_login'),
    url(r'^sort/(?P<pk>[\d]+).html', BlogSortContentListView.as_view(), name='sort_content'),
    
]
