from django.urls import path, include
from products.views import ProductListView, product_detail_view
app_name = 'products'

urlpatterns = [
    path('product/<sku:product_sku>/', product_detail_view, name='product_detail'),
    path('', ProductListView.as_view(), name='list')
]