from django.forms import ModelForm
from .models import ProductCommentModel


class ProductCommentModelForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review', 'email', 'rating']