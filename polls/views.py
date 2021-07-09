from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F # para actualizar modelos por diferentes request simultaneamente

from django.views import generic
from django.views.generic.base import TemplateView

from .models import Choice, Question

#%% ------------------------ Views from task -----------------------------------




#%% ----- original code NO generic views --------

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list' : latest_question_list,
#         }
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = { 'question' : question }
#     return render(request,'polls/detail.html', context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

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
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class ownerView(TemplateView):
    template_name = "polls/owner.html"
#%% ----- CON generic views --------

class IndexView(generic.ListView):  # herada de la vista genérica de listview
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView): # herada de la vista genérica de DetailView
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView): # herada de la vista genérica de DetailView
    model = Question
    template_name = 'polls/results.html'

class sessionView(TemplateView):
    template_name = 'polls/session_views.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        visits = self.request.session.get('num_visits',0) + 1
        self.request.session['num_visits'] = visits
        context['visits'] = visits
        return context

# def sessionView(request):
#     visits = request.session.get('num_visits',0) + 1
#     request.session['num_visits'] = visits
#     html_patt = '''<html>
#                     <head>
#                           <title>{} </title>
#                     </head>
#                     <body>
#                           {}
#                     </body>
#                     </html>'''
#     title = 'numero sesiones dj4e'
#     response = 'Numero de visitas a esta pagina es: '+str(visits)
#     url = '''<br><br>
#             <a href="{% url 'polls:index' %}">
#              come back to polls</a>'''
#     return HttpResponse(html_patt.format(title,response + url))



