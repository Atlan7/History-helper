import os
from PIL import Image

from django.db import models
from django.conf import settings
from pytils.translit import slugify

from django.urls import reverse_lazy


class Article(models.Model):
    title = models.CharField(max_length=300)
    card_img = models.ImageField(upload_to='articles/article_card', default='article/defalut_titile_img.jpg')
    title_img = models.ImageField(upload_to='articles/article_title', default='article/defalut_titile_img.jpg')
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    text = models.TextField()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='article_likes')
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='article_dislikes')

    def get_absloute_url(self):
        return reverse_lazy('articles:view-articlce', kwargs={'article_slug': self.slug})

    def save(self, *args, **kwargs): 
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


class Review(models.Model):
    article = models.ForeignKey(Article, related_name='reviews_to_article', on_delete=models.CASCADE)
    date_of_creating = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField('Comment', max_length=5000)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='review_likes')
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='review_dislikes')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

    def __str__(self):
        return f'{self.article.title} - {self.user}' 

    @property
    def children(self):
        return Review.objects.filter(parent=self).order_by('date_of_creating').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
