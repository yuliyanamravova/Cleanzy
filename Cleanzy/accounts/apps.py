from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Cleanzy.accounts'

    def ready(self):
        import Cleanzy.accounts.signals
