from django.shortcuts import get_object_or_404, render, reverse

# Create your views here.
# defines your views that u want ur app to have
from django.http import HttpResponse
from .models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# we want this to be the page shown when the browser goes to http://127.0.0.1:8000/polls/
def index(request):
    # get the 5 newest Question instances
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # latest_questions_text = [q.question_text for q in latest_question_list]
    # output = ', '.join(latest_questions_text)
    # return HttpResponse(output)

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) # Jinja?

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id) # get me question with id # and if it doesnt exist then 404 not found
    # basically find the thing or 404 not found
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # first check if we can get the choice for the question and match w/sent from browser
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
        return HttpResponseRedirect(reverse('results', args=(question.id,))) # 'polls:results'