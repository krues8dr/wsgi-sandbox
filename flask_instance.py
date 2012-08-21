import logging

from flask import Flask


def create_app(config_filename=None):
    "Use Flask's application factory pattern, to support playing in sandbox."
    app = Flask(__name__)

    if config_filename is not None:
        app.config.from_pyfile(config_filename)

    # Note log level here, as some log messages below will not be displayed.
    app.config['LOG_LEVEL'] = app.config.get('LOG_LEVEL', logging.WARNING)

    @app.route('/')
    def index():
        app.logger.debug('DEBUG log message from Flask at "/".')
        app.logger.info('INFO log message from Flask at "/".')
        app.logger.warning('WARNING log message from Flask at "/".')
        app.logger.error('ERROR log message from Flask at "/".')
        app.logger.critical('CRITICAL log message from Flask at "/".')
        return 'Flask: "Hello, world!"', 200, {'Content-Type': 'text/plain'}

    @app.before_first_request
    def setup_logging():
        """Set up logging for this application on the first request.

        This is in a before_first_request hook and not in create_app in the
        event that app.debug (or app.config['DEBUG']) is set between create_app
        and running the application.

        Flask has logging in debug mode, but does not have any log handlers in
        production -- such that Flask does not make assumptions about the
        production environment. As such, we only add a handler if we are not in
        debug mode.
        """
        if not app.debug:
            app.logger.addHandler(logging.StreamHandler())
            app.logger.setLevel(app.config['LOG_LEVEL'])

    return app


application = create_app()


if __name__ == '__main__':
    application.run()
