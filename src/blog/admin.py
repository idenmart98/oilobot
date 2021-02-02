from django.contrib import admin
from django.contrib.admin import ModelAdmin
from trumbowyg.widgets import TrumbowygWidget
from .models import Post, Category, Question
from django.forms import ModelForm


class PostAdminForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'body': TrumbowygWidget(),
        }

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Category)

admin.site.register(Post, PostAdmin)

admin.site.register(Question)