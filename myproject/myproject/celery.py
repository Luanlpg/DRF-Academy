from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define as configurações padrão do Django para o Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

# Carrega as configurações do Django no Celery usando namespace 'CELERY'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Procura por tasks automaticamente em todas as apps registradas no Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request}')