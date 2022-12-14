from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from url_creator.models import UrlSubmission
from .forms import UrlForm
from django.views.decorators.csrf import csrf_protect
from url_creator.available_url_db_helper import get_available_shortened_url_path
from urllib.parse import urlparse
from url_creator.url_submission_db_helper import create_and_save_shortened_url


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


@csrf_protect
def create_url(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            return create_and_save_shortened_url(request, form)
    return HttpResponse('invalid url')


def redirect_shortened_url(request, shortened_url_path):
    try:
        url_submission = UrlSubmission.objects.get(
        shortened_url_path=shortened_url_path)
    except UrlSubmission.DoesNotExist:
        url_submission = None
    if not url_submission:
        return HttpResponse('invalid url')
    response = HttpResponse("", status=302)
    response['Location'] = str(url_submission.url)
    return response
