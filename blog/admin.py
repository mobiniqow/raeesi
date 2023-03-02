from django.contrib import admin
from .models import Category, SubCategory, Post, Hashtag, HashtagNew, Comment

admin.site.register(Category)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)


admin.site.register(SubCategory, SubCategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at','views','state')
    list_filter = ('category',)


admin.site.register(Post, PostAdmin)
admin.site.register(Hashtag)
admin.site.register(HashtagNew)
admin.site.register(Comment)
