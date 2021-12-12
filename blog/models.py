from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Category(models.Model):
    title_ru = models.CharField(max_length=200,verbose_name = 'Заголовок на русском')
    image = models.ImageField(upload_to='images')
    title_kg = models.CharField(max_length=200,verbose_name = 'Заголовок на кыргызском')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title_ru

class Post(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name = 'Заголовок на русском')
    title_kg = models.CharField(max_length=200, verbose_name = 'Заголовок на кыргызском')
    body_ru = QuillField(verbose_name='Тело поста на русском')
    body_kg = QuillField(verbose_name='Тело поста на кыргызком')
    image = models.ImageField(upload_to='images', blank=True, null=True)
    slug_id = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title_ru}/{self.title_kg}'

class Question(models.Model):
    question_ru = models.CharField(max_length =50, verbose_name='Вопрос')
    answer_ru = models.TextField(blank = True, verbose_name='Ответ')

    question_kg = models.CharField(max_length =50, verbose_name='Суроо')
    answer_kg = models.TextField(blank = True, verbose_name='Жооп')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    
    def __str__(self):
        return self.question_ru




        