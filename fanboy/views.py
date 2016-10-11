from django.shortcuts import render
from fanboy.models import BriarPipe

# Create your views here.
def home_view(request):

    return render(request,'home.html')


def detail_view(request):

    pipes = BriarPipe.objects.all()


    return render(request, 'details.html', {'pipes':pipes})

def about_view(request):
    return render(request, 'about.html')