from django.db import models
from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models



class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=128,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'


class ProductTagModel(models.Model):
    name = models.CharField(max_length=128, )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Tag'
        verbose_name_plural = 'Product Tags'


class ProductColorModel(models.Model):
    name = models.CharField(max_length=128, )
    code = models.CharField(max_length=7)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Color'
        verbose_name_plural = 'Product Colors'


class ProductSizeModel(models.Model):
    name = models.CharField(max_length=128,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Size'
        verbose_name_plural = 'Product Sizes'

class ProductDimensionModel(models.Model):
    name = models.CharField(max_length=128,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Dimension'
        verbose_name_plural = 'Product Dimensions'

class ProductBrandModel(models.Model):
    name = models.CharField(max_length=128, )
    logo = models.ImageField(null=True, blank=True, upload_to='manufacture/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Brand'
        verbose_name_plural = 'Product Brands'


class ProductModel(models.Model):
    image = models.ImageField(upload_to='products/')

    name = models.CharField(max_length=255,)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0,
                                                validators=
                                                [MaxValueValidator(100), MinValueValidator(0)]
                                                )
    sku = models.CharField(max_length=10, unique=True)
    count = models.PositiveIntegerField()
    real_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    brand = models.ForeignKey(ProductBrandModel, on_delete=models.CASCADE, related_name='products')
    colors = models.ManyToManyField(ProductColorModel, related_name='products')
    tags = models.ManyToManyField(ProductTagModel, related_name='products')
    categories = models.ManyToManyField(ProductCategoryModel, related_name='products')
    sizes = models.ManyToManyField(ProductSizeModel, related_name='products')
    dimension = models.ManyToManyField(ProductDimensionModel, related_name='products' )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_discount(self):
        return self.discount != 0

    def is_available(self):
        return self.count != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.discount * self.price / 100

    def get_new(self):
        current_dateTime = datetime.now()
        current_dateTime = str(current_dateTime)
        created_at = str(self.created_at)
        d = created_at[9]+created_at[10]
        f = current_dateTime[9]+current_dateTime[10]
        f = int(f)
        d = int(d)
        if f - d < 3:
            return True
        else:
            return False


    def get_related_products(self):
        return ProductModel.objects.filter(categories=1).exclude(pk=self.pk)[:3]

    def is_cat():
        if self.categories == 'Laptop':
            return products

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImageModel(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

UserModel = get_user_model()

class ProductCommentModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
