from django.shortcuts import render
from django.views import View
from django.conf import settings

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations


class HomeView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, 'home/main.html', context)

class EjemploView1(View):

    def get(self,request):
        context = {}
        return render(request,'home/ejemplo1.html', context)


class EjemploView2(View):

    def get(self,request):
        context = {}
        return render(request,'home/ejemplo2.html', context)