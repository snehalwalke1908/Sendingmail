from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'
class BankConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bank'
