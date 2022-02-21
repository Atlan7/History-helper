from .models import Article


def add_like_to_the_article(request, article):
        if article.dislikes.filter(id=request.user.id).exists():
            article.dislikes.remove(request.user)
            article.likes.add(request.user)

        elif article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)

        else:
            article.likes.add(request.user)


def add_dislike_to_the_article(request, article):
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
            article.dislikes.add(request.user)

        elif article.dislikes.filter(id=request.user.id).exists():
            article.dislikes.remove(request.user)

        else:
            article.dislikes.add(request.user)


def add_like_to_the_article_review(request, review):
        if review.dislikes.filter(id=request.user.id).exists():
            review.dislikes.remove(request.user)
            review.likes.add(request.user)

        elif review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)

        else:
            review.likes.add(request.user)


def add_dislike_to_the_article_review(request, review):
        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
            review.dislikes.add(request.user)

        elif review.dislikes.filter(id=request.user.id).exists():
            review.dislikes.remove(request.user)

        else:
            review.dislikes.add(request.user)
