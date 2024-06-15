from django.urls import path, include
from products.views import ProductsListView, ProductDetailView, ProductCommentView, add_or_remove, add_or_remove_likes
app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('cart/<int:pk>/', add_or_remove, name='add-or-remove'),
    path('likes/<int:pk>/', add_or_remove_likes, name='add-or-remove-likes'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('comment/<int:pk>/', ProductCommentView.as_view(), name='comment'),

]