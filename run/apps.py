from django.apps import AppConfig


class RunConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'run'

    def ready(self):
        import run.handlers