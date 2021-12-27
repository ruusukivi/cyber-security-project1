import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse


from .models import Choice, Question, Feedback


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    feedback_list = Feedback.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
        'feedback_list': feedback_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def feedback(request):
    if request.method == "POST":
        feedb = Feedback()
        feedb.text = request.POST['text']
        feedb.nickname = request.POST['nickname']
        feedb.pub_date = datetime.datetime.now()
        feedb.save()
    return redirect("/")


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
