from django.conf import settings

if settings.APP_NAME == 'edc_visit_tracking':
    from .tests import models
