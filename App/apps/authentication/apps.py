import re

from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.authentication'

    def ready(self):
        try:
            from django.contrib.sites.models import Site
            from core.settings import SERVER
            site = Site.objects.filter(domain=SERVER)
            if site.count() == 0:
                site = Site.objects.create(domain=SERVER)
            else:
                site = site.first()
            with open('core/settings.py', 'r') as f:
                setting_contents = f.read()
            with open('core/settings.py', 'w') as f:
                if 'SITE_ID' in setting_contents:
                    final_setting = re.sub(r'SITE_ID[ ]*=[ ]*[0-9]+',f'SITE_ID = {site.id}', setting_contents)
                else:
                    final_setting = setting_contents + '\n' + f'SITE_ID = {site.id}'
                f.write(final_setting)
        except Exception as _:
            pass
