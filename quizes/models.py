from django.db import models

from articles.models import Article


class Quiz(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    number_of_questions = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.article.title

    def get_question(self):
        return self.question_set.all()


class Question(models.Model): 
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answer_set.all()

    def get_correct_answer(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=500)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'вопрос: {self.question.text}, ответ: {self.text}, правильный: {self.correct}'


class Results(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey
    score = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.pk
