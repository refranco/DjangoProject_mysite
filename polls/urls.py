from django.urls import path

from . import views

app_name = 'polls'

#%% --- without GENERIC VIEWS ---
# urlpatterns = [
#       path('', views.index, name='index'),
#       path('owner', views.owner, name='owner'),
#       path('specifics/<int:question_id>/', views.detail, name ='detail'), # ex: /polls/5/
#       path('<int:question_id>/results/', views.results, name='results'), # ex: /polls/5/results/
#       path('<int:question_id>/vote/', views.vote, name='vote'), # ex: /polls/5/vote/
#       ]

#%% --- with GENERIC VIEWS ---
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('owner', views.ownerView.as_view(), name='owner'),
    path('owner/visits/',views.sessionView.as_view(), name='visitas'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # ex: /polls/5/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # ex: /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # ex: /polls/5/vote/
]