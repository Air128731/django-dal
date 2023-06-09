from dal.test.utils import fixtures

from django.apps import AppConfig
from django.db.models.signals import post_migrate


class TestApp(AppConfig):
    name = 'select2_djhacker_formfield'

    def ready(self):
        post_migrate.connect(fixtures, sender=self)
