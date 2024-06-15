from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from products.models import ProductModel
from django.views.generic import TemplateView, ListView, DetailView, CreateView


class HomePageView(ListView):
    template_name = 'home.html'
    model = ProductModel
    context_object_name = 'products'

    


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'

class AboutTemplateView(TemplateView):
    template_name = 'about-us.html'
