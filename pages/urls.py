from django.urls import path, include
from pages.views import HomePageView, ContactTemplateView, AboutTemplateView

app_name = 'pages'
urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("contact/", ContactTemplateView.as_view(), name='contact'),
    path("about-us/", AboutTemplateView.as_view(), name='about-us'),
]