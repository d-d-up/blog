from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class MyBlogListView(View):
    def get(self, request):
        return render(request, 'myblog_list.html')
