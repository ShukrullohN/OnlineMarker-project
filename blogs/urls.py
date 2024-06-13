from django.urls import path, include
from blogs.views import BlogListView
app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='list')
]