# Generated by Django 4.0.2 on 2022-02-21 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('card_img', models.ImageField(default='article/defalut_titile_img.jpg', upload_to='articles/article_card')),
                ('title_img', models.ImageField(default='article/defalut_titile_img.jpg', upload_to='articles/article_title')),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('text', models.TextField()),
                ('dislikes', models.ManyToManyField(blank=True, null=True, related_name='article_dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, null=True, related_name='article_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creating', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(max_length=5000, verbose_name='Comment')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_to_article', to='articles.article')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='review_dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='review_likes', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='articles.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
