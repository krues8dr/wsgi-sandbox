import logging


logger = logging.getLogger('wsgi_instance')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARNING)


def application(environ, start_response):
    logger.debug('DEBUG log message from WSGI application at "/".')
    logger.info('INFO log message from WSGI application at "/".')
    logger.warning('WARNING log message from WSGI application at "/".')
    logger.error('ERROR log message from WSGI application at "/".')
    logger.critical('CRITICAL log message from WSGI application at "/".')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['WSGI application says, "Hello, world!"\n']
