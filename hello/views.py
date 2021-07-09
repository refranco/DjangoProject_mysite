from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# -- session manage in class mode ---
# class myview(TemplateView):
#     template_name = 'polls/session_views.html'

#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         visits = self.request.session.get('num_visits',0) + 1
#         self.request.session['num_visits'] = visits
#         context['visits'] = visits
#         return context

# ---- genereal function mode --------
def myview(request):
    response = HttpResponse()
    visits = request.session.get('num_visits',0) + 1
    request.session['num_visits'] = visits
    if visits > 4: del(request.session['num_visits'])
    response.write('view count='+str(visits))
    response.set_cookie('dj4e_cookie', '9978f8c4', max_age=1000)
    return response