import logging

from flask import Flask


def create_app(config_filename=None):
    app = Flask(__name__)

    if config_filename is not None:
        app.config.from_pyfile(config_filename)

    app.config['LOG_LEVEL'] = app.config.get('LOG_LEVEL', logging.WARNING)

    @app.route('/')
    def index():
        app.logger.debug('DEBUG log message from Flask at "/".')
        app.logger.info('INFO log message from Flask at "/".')
        app.logger.warning('WARNING log message from Flask at "/".')
        app.logger.error('ERROR log message from Flask at "/".')
        app.logger.critical('CRITICAL log message from Flask at "/".')
        return 'Flask says, "Hello, world!"'

    @app.before_first_request
    def setup_logging():
        if not app.debug:
            app.logger.addHandler(logging.StreamHandler())
            app.logger.setLevel(app.config['LOG_LEVEL'])

    return app


application = create_app()


if __name__ == '__main__':
    application.run()
