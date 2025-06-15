from django.apps import AppConfig


class CakeShopApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cake_shop_application'
    def ready(self):
        from . import signals
