from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=128, verbose_name=('name'))
    image = models.ImageField(upload_to='blog-authors')
    about = models.TextField(verbose_name=('name'))
    position = models.CharField(max_length=128, verbose_name=('position'))
    profession = models.CharField(max_length=128, verbose_name=('profession'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('author')
        verbose_name_plural = ('authors')


class BlogCategoryModel(models.Model):
    name = models.CharField(max_length=128, verbose_name=('name'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('categories')


class BlogTagModel(models.Model):
    name = models.CharField(max_length=128, verbose_name=('name'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('tag')
        verbose_name_plural = ('tags')


class BlogModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=('title'))
    image = models.ImageField(upload_to='blog-images')
    short_info = models.TextField(null=True, verbose_name=('short_info'))
    content = models.TextField()
    categories = models.ManyToManyField(BlogCategoryModel, related_name='blogs')
    tags = models.ManyToManyField(BlogTagModel, related_name='tags')
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='blogs')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('blog')
        verbose_name_plural = ('blogs')