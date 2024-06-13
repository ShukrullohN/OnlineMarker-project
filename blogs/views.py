from django.shortcuts import render
from django.views.generic import TemplateView, CreateView


class BlogListView(TemplateView):
    template_name = 'blog-list.html'

