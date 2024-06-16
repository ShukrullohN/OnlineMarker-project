from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from products.models import ProductModel
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from pages.forms import ContactModelForm


class HomePageView(ListView):
    template_name = 'home.html'
    model = ProductModel
    context_object_name = 'products'

    


class ContactTemplateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_url = '/'

class AboutTemplateView(TemplateView):
    template_name = 'about-us.html'
