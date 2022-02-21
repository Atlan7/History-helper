from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(
        label='Комментарий',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows':5,
                'cols':15,
                'placeholder':'Оставь своё мнение о статье.'
            }
        )
    )

    class Meta:
        model = Review
        fields = ('comment',)


class ReplyToReviewForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows':5,
                'cols':15,
                'placeholder':'Ответь на комментарий.'
            }
        )
    )

    class Meta:
        model = Review
        fields = ('comment',)
