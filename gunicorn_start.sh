#!/bin/bash

NAME="stages"                              #Name of the application (*)
DJANGODIR=/var/www/stages             # Django project directory (*)
SOCKFILE=/var/www/stages/run/gunicorn.sock        # we will communicate using this unix socket (*)
USER=www-data                                        # the user to run as (*)
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_WSGI_MODULE=stages.wsgi                     # WSGI module name (*)

echo "Lancement de $NAME en tant que `whoami`"

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
cd $DJANGODIR
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE
