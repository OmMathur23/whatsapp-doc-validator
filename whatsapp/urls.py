from django.urls import path
from . import webhook_views  # or views_webhook if that's what you named it

urlpatterns = [
    path('', webhook_views.whatsapp_webhook, name='whatsapp_webhook'),
]
