from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def homepage(request):
    return HttpResponse('Create')

def redirect_shortened_url(request, shortened_url):
    return HttpResponse(shortened_url)
    # return HttpResponseRedirect('https://www.google.com')
