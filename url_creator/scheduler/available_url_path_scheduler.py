from url_creator.available_url_db_helper import add_new_available_paths, number_of_available_urls, require_more_url_paths
import sys
from django_apscheduler.jobstores import DjangoJobStore, register_events
from apscheduler.schedulers.background import BackgroundScheduler


# This is the function you want to schedule - add as many as you want and then register them in the start() function below


def replenish_shortened_url_paths():
    print('number_of_available_urls=' + str(number_of_available_urls()))
    if require_more_url_paths():
        add_new_available_paths(1000)
    # from url_creator.models import ShortenedUrlPath
    # ShortenedUrlPath.objects.all().delete()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(replenish_shortened_url_paths, 'interval', seconds=5,
                      name='replenish_urls', jobstore='default')
    register_events(scheduler)
    scheduler.start()
