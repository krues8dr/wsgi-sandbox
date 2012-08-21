import logging


logger = logging.getLogger('wsgi_instance')
logger.addHandler(logging.StreamHandler())
# Note log level here, as some log messages below will not be displayed.
logger.setLevel(logging.WARNING)


def application(environ, start_response):
    """The simplest WSGI application, with logging for demonstration."""
    logger.debug('DEBUG log message from WSGI application at "/".')
    logger.info('INFO log message from WSGI application at "/".')
    logger.warning('WARNING log message from WSGI application at "/".')
    logger.error('ERROR log message from WSGI application at "/".')
    logger.critical('CRITICAL log message from WSGI application at "/".')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['WSGI application: "Hello, world!"\n']
