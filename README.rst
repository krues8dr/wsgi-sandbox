==============
 WSGI Sandbox
==============

This project contains some WSGI deployment demonstrations using Python 2.7.3.

Motivation:

1. Deploy standalone WSGI applications with a solid httpd proxy in front.
2. Support gracefully reloading application code without dropping any requests.
3. Configure WSGI applications with production loggers.
4. Have all loggers go to a single destination, per application.
5. Rotate log files with a simple configuration.
6. Keep all production configuration in once place.

Demonstration:

1. Set up gunicorn with nginx proxying in front.
2. Run gunicorn via supervisord, gracefully reload with pid from supervisorctl.
3. Configure Python's standard library logging to each WSGI application.
4. Use stderr logging handlers, pass through gunicorn, capture with supervisor.
5. Rotate log files with supervisord.
6. Put all production configuration in supervisord.conf.

Install Python dependencies in a virtualenv::

    pip install -r requirements.txt

Kick everything off by starting supervisor::

    supervisord

Proxy via nginx::

    nginx -p . -c nginx.conf

Generate a lot of concurrent requests in order to see some action::

    ab -c 10 -n 10000 http://flask.local.willowtreeapps.com:8000/
    ab -c 10 -n 10000 http://django.local.willowtreeapps.com:8000/
    ab -c 10 -n 10000 http://wsgi.local.willowtreeapps.com:8000/

This generates 10000 requests with a concurrency level of 10, using ab
(ApacheBench). Docs are at http://httpd.apache.org/docs/2.4/programs/ab.html.

On Ubuntu::

    sudo apt-get install apache2-utils

To gracefully reload gunicorn::

    kill -HUP `supervisorctl pid flask_instance`
    kill -HUP `supervisorctl pid django_instance`
    kill -HUP `supervisorctl pid wsgi_instance`

A note on following the logs. ``supervisorctl`` provides a useful tail command,
which supports ``tail -f``. However, it's buffered by default. If you want to
see some action, instead of e.g. ``supervisorctl tail -f flask_instance``, use
``tail -f flask_instance.log`` directly.
