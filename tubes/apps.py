from django.apps import AppConfig


class TubesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tubes'

    def ready(self):
        import tubes.handlers
