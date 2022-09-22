from url_creator.available_url_db_helper import add_new_available_paths, number_of_available_urls, require_more_url_paths
import sys
from django_apscheduler.jobstores import DjangoJobStore, register_events
from apscheduler.schedulers.background import BackgroundScheduler
import os

DELAY_AVAILABLE_URL_PATH_CHECK_S = os.environ.get(
    'NUM_NEW_AVAILABLE_URL_PATHS', 10)


def replenish_shortened_url_paths():
    print('available_url_db_helper.py number_of_available_urls=' + str(number_of_available_urls()))
    if require_more_url_paths():
        add_new_available_paths(5)

    # from url_creator.models import ShortenedUrlPath
    # ShortenedUrlPath.objects.all().delete()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(
        replenish_shortened_url_paths,
        'interval',
        seconds=int(DELAY_AVAILABLE_URL_PATH_CHECK_S),
        name='replenish_urls', 
        id='h8nhc0re',
        jobstore='default',
        replace_existing=True,)
    scheduler.start()

