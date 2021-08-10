from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import Cat, Breed
# Create your views here.

class MainView(LoginRequiredMixin, View):
      template_name = 'cats/cat_list.html'
      def get(self, request):
            breed_count = Breed.objects.all().count()
            cat_list = Cat.objects.all()
            context = {'cat_list':cat_list,'breed_count':breed_count}
            return render(request,self.template_name, context)

class BreedView(LoginRequiredMixin, View):
      template_name = 'cats/breed_list.html'

      def get(self, request):
            breed_list = Breed.objects.all()
            breed_counts = []
            for breed in breed_list:
                  breed_num = Cat.objects.filter(breed=breed).count()
                  breed_counts.append((breed,breed_num))
            context ={'breed_list':breed_list,'breed_counts':breed_counts}
            return render(request,self.template_name,context)

# ---- Breed veiws -----

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    template = 'cats/breed_confirm_delete.html'
    success_url = reverse_lazy('cats:all')

# ---- cats views ---

class CatCreate(LoginRequiredMixin, CreateView):
      model = Cat
      fields = '__all__'
      success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin,UpdateView):
      model = Cat
      fields = '__all__'
      success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
      model = Cat
      fields = '__all__'
      success_url = reverse_lazy('cats:all')
      template = 'cats/cat_confirm_delete.html'
