==============
 WSGI Sandbox
==============

This project contains some WSGI deployment demonstrations using Python 2.7.3.

Install Python dependencies in a virtualenv::

    pip install -r requirements.txt

Kick everything off by starting supervisor::

    supervisord

Proxy via nginx::

    nginx -p . -c nginx.conf
