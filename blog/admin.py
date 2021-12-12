from django.contrib import admin
from .models import Post, Category, Question

 

admin.site.register(Category)

# admin.site.register(Question)


@admin.register(Post)
class QuillPostAdmin(admin.ModelAdmin):
    pass
