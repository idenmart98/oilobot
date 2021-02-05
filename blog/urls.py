from django.contrib import admin
from .views import (
    questions_view, 
    answer_view, 
    index, 
    post_view,
    category_view,
    post_details,
    category_details, 
    index_kg)
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('', index_kg),
    path('<str:lang>', index),
    path('questions/<str:lang>', questions_view),
    path('answer/<int:answer_id>/<str:lang>', answer_view),
    path('post/<str:lang>',post_view,name='post'),
    path('category/<str:lang>',category_view,name='category'),
    path('post_details/<int:post_id>/<str:lang>',post_details,name='post_details'),
    path('category/<int:cat_id>/<str:lang>', category_details, name = 'cat_details'),
]