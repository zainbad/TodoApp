from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .signals import customer_profile


class TodoConfig(AppConfig):
    name = 'todo'

    # def read(self):
    #     post_save.connect(customer_profile, sender=User)
