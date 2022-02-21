from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView, DetailView, CreateView, View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Article, Review
from quizes.models import Quiz
from .service import (
        add_like_to_the_article,
        add_dislike_to_the_article,
        add_like_to_the_article_review,
        add_dislike_to_the_article_review,
)

from .forms import ReviewForm, ReplyToReviewForm


class ArticlesListView(ListView):
    model = Article 
    template_name = 'articles/view_articles.html'
    context_object_name = 'articles'


class SearchArticle(View):
    def get(self, request):
        name_of_necessary_article = request.GET.get('search')
        articles = Article.objects.filter(title__icontains=name_of_necessary_article)
        if articles:
            return render(request, 'articles/view_articles.html', {'articles':articles})

        messages.error(request, 'Нет подходящих результатов.')
        return HttpResponseRedirect(reverse_lazy('articles:view-articles'))


class ViewArticle(DetailView):
    model = Article
    template_name = 'articles/view_article.html'
    context_object_name = 'article'
    slug_field = 'slug'
    slug_url_kwarg = 'article_slug'

    def get_context_data(self, **kwargs):
        """Adding the Review form and Reviews"""
        context = super().get_context_data(**kwargs)
        article = context.get('article')

        # Adding article reviews
        reviews = Review.objects.filter(article=article).order_by('-date_of_creating')
        context['reviews'] = reviews

        quizes = Quiz.objects.get()

        # Adding review form
        form = ReviewForm()
        reply_form = ReplyToReviewForm()
        context['form'] = form
        context['reply_form'] = reply_form
        return context


class ViewQuizToArticle(LoginRequiredMixin, View):
    def post(self, request, template_name='quizes/create_quiz.html'):
        form = QuizForm(request.POST)
        
        if form.is_valid():
            try:
                context = get_questions(request, form)
            except ValueError as e:
                messages.error(self.request, e)
                return render(request, template_name, {'form': form})
            return render(request, template_name='quizes/created_quiz.html', context=context)
        return render(request, template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class AddLikeToArticle(LoginRequiredMixin, View):
    def post(self, request, article_slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=article_slug)
        add_like_to_the_article(request, article)
        return redirect(reverse_lazy('articles:view-article', args=[str(article.slug)]) + f'#likes_and_dislikes_for_article_{article.slug}')


class AddDislikeToArticle(LoginRequiredMixin, View):
    def post(self, request, article_slug, *args, **kwags):
        article = get_object_or_404(Article, slug=article_slug)
        add_dislike_to_the_article(request, article)
        return redirect(reverse_lazy('articles:view-article', args=[str(article.slug)]) + f'#likes_and_dislikes_for_article_{article.slug}')


class AddReviewToArticle(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm

    def post(self, request, article_slug):
        article = get_object_or_404(Article, slug=article_slug)
        user = request.user

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.article = article
            review.user = user
            review.save()

        return HttpResponseRedirect(reverse_lazy('articles:view-article', args=[str(article.slug)])+ f'#comment_{review.pk}')


class ReplyToReview(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReplyToReviewForm

    def post(self, request, article_slug, review_pk):
        article = get_object_or_404(Article, slug=article_slug)
        parent_review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        form = ReplyToReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.article = article
            review.user = user
            review.parent = parent_review
            review.save()
        return redirect(reverse_lazy('articles:view-article', args=[str(article.slug)]) + f'#comment_{review.pk}')


class AddLikeToReview(LoginRequiredMixin, View):
    def post(self, request, article_slug, review_pk, *args, **kwargs):
        article = get_object_or_404(Article, slug=article_slug)
        review = get_object_or_404(Review, pk=review_pk)
        add_like_to_the_article_review(request, review)
        return redirect(reverse_lazy('articles:view-article', args=[str(article.slug)]) + f'#comment_{review.pk}')


class AddDislikeToReview(LoginRequiredMixin, View):
    def post(self, request, article_slug, review_pk):
        article = get_object_or_404(Article, slug=article_slug)
        review = get_object_or_404(Review, pk=review_pk)
        add_dislike_to_the_article_review(request, review)
        return redirect(reverse_lazy('articles:view-article', args=[str(article.slug)]) + f'#comment_{review.pk}')
