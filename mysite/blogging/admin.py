from django.contrib import admin
from blogging.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts', )

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

