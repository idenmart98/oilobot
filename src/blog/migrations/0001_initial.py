# Generated by Django 3.1.6 on 2021-02-04 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200, verbose_name='Заголовок на русском')),
                ('title_kg', models.CharField(max_length=200, verbose_name='Заголовок на кыргызском')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=5, verbose_name='Вопрос')),
                ('answer', models.TextField(blank=True, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопросы',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200, verbose_name='Заголовок на русском')),
                ('title_kg', models.CharField(max_length=200, verbose_name='Заголовок на кыргызском')),
                ('body_ru', models.TextField(max_length=1500, verbose_name='Тело поста на русском')),
                ('body_kg', models.TextField(max_length=1500, verbose_name='Тело поста на кыргызском')),
                ('pic_of_women', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
