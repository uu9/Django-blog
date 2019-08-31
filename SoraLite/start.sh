#!/bin/sh
nginx -g 'daemon off;'&uwsgi --ini /web/uwsgi.ini;
exec /bin/sh;