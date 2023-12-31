from django.apps import AppConfig


class ImagetstConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'imagetst'

    def ready(self):
        import imagetst.signals
