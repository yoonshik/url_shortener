from django.apps import AppConfig


class UrlCreatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'url_creator'

    def ready(self):
        from .scheduler import available_url_path_scheduler
        available_url_path_scheduler.start()