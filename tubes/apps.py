from django.apps import AppConfig


class TubesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tubes'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Tube'))
        registry.register(self.get_model('TubeBatch'))
        registry.register(self.get_model('TubeBatchPosition'))
        import tubes.handlers
