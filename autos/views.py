from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Make, Auto
# Create your views here.

# Main View Here ----
class MainView(LoginRequiredMixin, View):
    
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = {'make_count':mc,'auto_list':al}
        return render(request,'autos/auto_list.html',ctx)

# ---- makes views -------------
class MakeView(LoginRequiredMixin, View):
    
    def get(self, request):
        mc = Make.objects.all()
        mc_counts = []
        for make in mc:
            auto_mc = Auto.objects.filter(make=make).count()
            mc_counts.append((make, auto_mc))
        ctx = {'mc_counts':mc_counts,'make_list':mc}
        return render(request,'autos/make_list.html',ctx)


class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    template = 'autos/make_confirm_delete.html'
    success_url = reverse_lazy('autos:all')

# ----- Autos views -------------

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    template = 'autos/auto_form.html'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
