from django.db import models

class UrlSubmission(models.Model):
    url = models.CharField(max_length=255)
    shortened_url_path = models.CharField(max_length=50)
    submission_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shortened_url_path + ' --> ' + self.url

class ShortenedUrlPath(models.Model):
    shortened_url_path = models.CharField(max_length=50)
    in_use = models.BooleanField()
    creation_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shortened_url_path + ' : ' + self.in_use