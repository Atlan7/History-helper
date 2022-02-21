from django.urls import path
from .views import (
        ArticlesListView, SearchArticle, ViewArticle, AddReviewToArticle , 
        AddLikeToArticle, AddDislikeToArticle, ReplyToReview, AddLikeToReview, AddDislikeToReview 
    )

urlpatterns = [
    path('', ArticlesListView.as_view(), name='view-articles'),
    path('search-article', SearchArticle.as_view(), name='search-article'),

    path('view-article/<slug:article_slug>', ViewArticle.as_view(), name='view-article'),
    path('review-to-article/<slug:article_slug>', AddReviewToArticle.as_view(), name='review-article'),
    path('like-article/<slug:article_slug>', AddLikeToArticle.as_view(), name='like-article'),
    path('dislike-article/<slug:article_slug>', AddDislikeToArticle.as_view(), name='dislike-article'),

    path('add-reply-to-review/<slug:article_slug>/<int:review_pk>', ReplyToReview.as_view(), name='reply-to-review'),
    path('like-review-article/<slug:article_slug>/<int:review_pk>', AddLikeToReview.as_view(), name='like-review'),
    path('dislike-review-article/<slug:article_slug>/<int:review_pk>', AddDislikeToReview.as_view(), name='dislike-review'),
]
