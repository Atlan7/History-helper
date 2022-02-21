from django import forms

from .models import Quiz


class QuizForm(forms.Form):
    articles = forms.ModelMultipleChoiceField(
        label="Выберите статьи для теста", 
        queryset=Quiz.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control js-example-basic-multiple'
            }
        )
    )
    quantity_questions = forms.IntegerField(
        label="Введите кол-во вопросов которые хотите прорешать.", 
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        )
    ) 
