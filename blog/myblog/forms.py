from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import BlogContent, BlogSort


class BlogContentCreateForm(forms.ModelForm):
    """博客内容创建表单"""
    def __init__(self, *args, **kwargs):
        super(BlogContentCreateForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        """定义规则字段."""
        model = BlogContent
        fields = ('title', 'sort', 'content')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'