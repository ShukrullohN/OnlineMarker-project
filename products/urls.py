from django.urls import path, include
from products.views import ProductsListView, ProductDetailView
app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
]