from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages 
from django.shortcuts import render
from django.views.generic import FormView

from .forms import QuizForm 
from .services import get_questions, results_of_quiz

import json


class Quiz(FormView):
    form_class = QuizForm
    template_name = 'quizes/create_quiz.html'
    context_object_name = 'questions'

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


class ViewQuizResults(FormView):
    form_class = QuizForm
    template_name = 'quizes/view_results.html'
    context_object_name = 'questions'

    def post(self, *args, **kwargs):
        if self.request.method == "POST":
            list_of_answers = json.loads(self.request.POST.dict()['list_of_answers'])
            res_of_quiz, right_answ, total_questions = results_of_quiz(list_of_answers) 
            html = render_to_string('quizes/view_results.html', {'res_of_quiz': res_of_quiz,'right_answ': right_answ, 'total_questions': total_questions})
            return JsonResponse(html, safe=False)

        return JsonResponse({"error": ""}, status=400)
