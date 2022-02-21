from .models import Question, Answer


def querySet_to_list(qs):
     return [i['id'] for i in qs]


def get_questions(request, form):
    context = {'form': form} 
    articles_ids = list(form.cleaned_data['articles'].values_list('id', flat=True))
    quantity_questions = form.cleaned_data['quantity_questions']

    pks_of_avalible_questions = []

    for i in range(len(articles_ids)):
        questions = Question.objects.filter(quiz=articles_ids[i]).values('id')
        pks_of_avalible_questions.extend(querySet_to_list(questions))
        
    
    if quantity_questions > len(pks_of_avalible_questions):
        if len(articles_ids) > 1:
            raise ValueError(f"Для данных статей максимальное кол-во вопросов: {len(pks_of_avalible_questions)}")
        else:
            raise ValueError(f"Для данной статьи максимальное кол-во вопросов: {len(pks_of_avalible_questions)}")
    else: 
        questions = []

        for i in range(quantity_questions):
            questions.append(Question.objects.get(pk=pks_of_avalible_questions[i]))


        context['questions'] = questions  

    return context


def results_of_quiz(answers):
    results = []
    total_questions = 0
    total_right_answers = 0

    for i in range(len(answers)):
        right_answer = [answer.id for answer in Question.objects.get(id=answers[i][0]).get_answers() if answer.correct]
        if answers[i][1] != 'None':
            gotten_answer = Answer.objects.get(id=answers[i][1])    
        right_answer = Answer.objects.get(id=right_answer[0])


        if right_answer == gotten_answer:
            total_right_answers += 1
            results.append([right_answer, right_answer])
        elif right_answer != gotten_answer: 
            results.append([right_answer, gotten_answer])
        else:
            results.append([right_answer, 'None'])

        total_questions +=1

    return results, total_right_answers, total_questions

