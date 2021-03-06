# Log handlers are configured in settings.py.

import logging

from django.http import HttpResponse


logger = logging.getLogger('django_instance')


def index(request):
    logger.debug('DEBUG log message from Django at "/".')
    logger.info('INFO log message from Django at "/".')
    logger.warning('WARNING log message from Django at "/".')
    logger.error('ERROR log message from Django at "/".')
    logger.critical('CRITICAL log message from Django at "/".')
    return HttpResponse('Django: "Hello, world!"', content_type='text/plain')
