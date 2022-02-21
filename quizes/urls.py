from django.urls import path

from .views import Quiz, ViewQuizResults


urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('view_results/', ViewQuizResults.as_view(), name='view-results-of-quiz'),
]
