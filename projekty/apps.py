from django.apps import AppConfig


class ProjektyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projekty'

    def ready(self) -> None:
        import projekty.user_classes
    