from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from products.forms import ProductCommentModelForm
from products.models import *


class ProductsListView(ListView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'
    paginate_by = 2


    def get_queryset(self):
        products = self.model.objects.all().order_by('-created_at')
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')
        col = self.request.GET.get('col')
        brand = self.request.GET.get('brand')
        dim = self.request.GET.get('dim')
        size = self.request.GET.get('size')
        sort = self.request.GET.get('sort')
        q = self.request.GET.get('q')

        if tag:
            products = products.filter(tags__in=tag)
        if cat:
            products = products.filter(categories__in=cat)
        if col:
            products = products.filter(colors__in=col)
        if brand:
            products = products.filter(brand__in=brand)
        if dim:
            products = products.filter(dimension__in=dim)
        if size:
            products = products.filter(sizes__in=size)
        if sort:
            if sort == '-price':
                products = products.order_by('-real_price')
            else:
                products = products.order_by('real_price')
        if q:
            products = products.filter(name__icontains=q)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategoryModel.objects.all()
        context['brands'] = ProductBrandModel.objects.all()
        context['dimension'] = ProductDimensionModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['colors'] = ProductColorModel.objects.all()
        context['sizes'] = ProductSizeModel.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = 'products/product-detail.html'
    model = ProductModel
    context_object_name = 'product'

    

    def get_context_data(self, *, object_list=None,  **kwargs):
        product = ProductModel.objects.get(id=self.kwargs["pk"])
        context = super().get_context_data(**kwargs)
        context.update({
            'comments': product.comments.all(),
            'products': ProductModel.objects.all(),
            'categories': ProductCategoryModel.objects.all(),
            'brands': ProductBrandModel.objects.all(),
            'dimensions': ProductDimensionModel.objects.all(),
            'sizes': ProductSizeModel.objects.all(),
            'tags': ProductTagModel.objects.all(),
            'colors': ProductColorModel.objects.all(),
        })
        return context


def add_or_remove(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)

    else:
        cart.append(pk)

    request.session['cart'] = cart
    return redirect(request.GET.get('next', 'products:list'))


def add_or_remove_likes(request, pk):
    likes = request.session.get('likes', [])
    if pk in likes:
        likes.remove(pk)

    else:
        likes.append(pk)

    request.session['likes'] = likes
    return redirect(request.GET.get('next', 'products:list'))


def create_review(request):
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    to = request.GET.get('to', '/')
    if request.method == 'POST':
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.product = product
            f.save()
            return redirect(to)
    return redirect('/')