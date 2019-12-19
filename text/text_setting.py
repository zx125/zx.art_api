import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wechat.settings.dev")

django.setup()

from django.conf import settings
print(settings)