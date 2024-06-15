from django.contrib import admin
from blogs.models import BlogCategoryModel, BlogModel, AuthorModel, BlogTagModel

@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at',)
    search_fields = ('name',)
    list_filter = ( 'created_at',)

@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at',)
    search_fields = ('name',)
    list_filter = ( 'created_at',)


@admin.register(BlogTagModel)
class BlogTagModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at',)
    search_fields = ('name',)
    list_filter = ( 'created_at',)

@admin.register(BlogModel)
class BlogModel(admin.ModelAdmin):
    list_display = ('title','created_at',)
    search_fields = ('title', 'content',)
    list_filter = ( 'created_at',)