from django.contrib import admin
from .models import Post, Category, Question

 

admin.site.register(Category)

admin.site.register(Post)

admin.site.register(Question)
