from django.shortcuts import render, redirect

# Create your views here.
from cms.models import Text, Title


def index(request, slug):
    path = request.path[7:8]
    texts = Text.objects.all().order_by('number')
    contents = Text.objects.get(id=slug)
    return render(request, 'index.html', {'texts': texts, 'conts': contents,'title' : Title.objects.all().first(),'check':int(path)})


def redir(request):
    return redirect('/index/2')
