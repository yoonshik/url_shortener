from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from url_creator.models import UrlSubmission
from url_shortener_service.forms import UrlForm
from django.views.decorators.csrf import csrf_protect
from url_creator.available_url_db_helper import get_available_shortened_url_path
from urllib.parse import urlparse


def create_and_save_shortened_url(form):
    print('create_and_save_shortened_url')
    url = form.cleaned_data['url']
    if '://' not in url:
        url = 'http://' + url
    if not is_valid_url(url):
        return HttpResponse('INVALID URL')

    shortened_url_path = get_available_shortened_url_path()
    url_submission = UrlSubmission(
        url=url, shortened_url_path=shortened_url_path)
    url_submission.save()
    return HttpResponse('Saved ' + url + ' TO ' + shortened_url_path)


def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
