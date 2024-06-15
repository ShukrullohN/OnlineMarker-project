from django.urls import path, include
from products.views import ProductsListView, ProductDetailView, ProductCommentView
app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('comment/<int:pk>/', ProductCommentView.as_view(), name='comment'),

]