from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UrlForm
from django.views.decorators.csrf import csrf_protect

def index(request):
    context = {}
    return render(request, 'index.html', context=context)

@csrf_protect
def create_url(request):
    if request.method == 'POST':
      form = UrlForm(request.POST)
      if form.is_valid():
        return HttpResponse('valid url')
    return HttpResponse('invalid url')

def redirect_shortened_url(request, shortened_url):
    return HttpResponse(shortened_url)
    # return HttpResponseRedirect('https://www.google.com')
