from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls.base import reverse_lazy
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Ad, Comment
from .forms import CreateForm, CommentForm
from .owner import OwnerCreateView, OwnerListView, OwnerDetailView, OwnerDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "ads/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = "ads/ad_detail.html"
    def get(self,request,pk):
        adx = Ad.objects.get(id=pk)
        comments = Comment.objects.filter(ad=adx).order_by('-updated_at')
        comment_form = CommentForm()
        ctx = {'ad':adx,'comments':comments,'comment_form':comment_form}
        return render(request, self.template_name, ctx)


class AdCreateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url=reverse_lazy('ads:all')
    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form':form}
        return render(request, self.template_name, ctx)
    
    def post(self,request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form':form}
            return render(request, self.template_name,ctx)
        
        ad = form.save(commit=False)
        ad.owner = self.request.user
        ad.save()
        return redirect(self.success_url)

class AdUpdateView(LoginRequiredMixin,View):
    template_name = 'ads/ad_form.html'
    success_url=reverse_lazy('ads:all')

    def get(self,request, pk):
        ad = get_object_or_404(Ad,id=pk, owner=self.request.user)
        form = CreateForm(instance=ad)
        ctx = {'form':form}
        return render(request,self.template_name, ctx)

    def post(self,request,pk=None):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad) 

        if not form.is_valid():
            ctx = {'form':form}
            return render(request, self.template_name,ctx)
        ad = form.save(commit=False)
        ad.save()
        return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad

def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response

class CommentCreateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_detail.html'

    def post(self,request, pk):

        adx = get_object_or_404(Ad,id=pk)
        print(request.POST)
        comment = Comment(text=request.POST['comment'], ad=adx, owner=request.user)
        comment.save()
        return redirect(reverse('ads:ad_detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
# https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ad = self.object.ad
        return reverse('ads:ad_detail', args=[ad.id])
