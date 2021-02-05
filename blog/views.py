from django.shortcuts import render
from .models import Question, Post, Category


def questions_view(request, lang):
    if lang == 'ru':
        return render(request, 'questions_ru.html', {'questions':Question.objects.all(), 'lang': 'ru'})
    return render(request, 'questions_kg.html', {'questions':Question.objects.all(), 'lang': 'kg'})

def index(request, lang):
    if lang == 'ru':
        return render(request, 'index_ru.html')
    return render(request, 'index_kg.html')

def index_kg(request):
    return render(request, 'index_kg.html')

def answer_view(request, answer_id, lang):
    answer = Question.objects.get(id=answer_id)
    if lang == 'ru':
        return render(request, 'answer.html', {'answer':answer.answer_kg, 'lang':'ru'})
    return render(request, 'answer.html', {'answer':answer.answer_kg, 'lang':'ru'})

def post_view(request, lang):
    posts = Post.objects.all()
    if lang == 'kg':
        return render(request, 'post_kg.html', context = {'posts':posts})
    
    return render(request, 'post.html', context = {'posts':posts})

def category_view(request, lang):
    categories = Category.objects.all()
    if lang == 'kg':
        return render(request, 'category_kg.html', context = {'categories':categories})
    
    return render(request, 'category.html', context = {'categories':categories})
 
def post_details(request,post_id, lang):
    post = Post.objects.get(id=post_id)
    if lang == 'kg':
        return render(request, 'post_details_kg.html', context = {'post':post})
    
    return render(request, 'post_details.html', context = {'post':post})


def category_details(request, cat_id, lang):
    posts = Post.objects.filter(category__id = cat_id)
    if lang == 'kg':
        return render(request, 'post_kg.html', context = {'posts':posts})
    
    return render(request, "post.html", context = {"posts":posts}) 

