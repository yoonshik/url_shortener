from django.db import models

class UrlSubmission(models.Model):
    url = models.CharField(max_length=255)
    shortened_url_path = models.CharField(max_length=50)
    submission_time = models.DateTimeField(auto_now=True)
