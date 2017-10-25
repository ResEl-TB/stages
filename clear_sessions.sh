#!/usr/bin/env bash
cd /srv/www/stages.resel.fr
echo '>>> Cleaning Django sessions\n'
/srv/www/stages.resel.fr/env/bin/python manage.py clearsessions
echo '[executed]\n'

echo '\n>>> Cleaning django-cas-ng sessions\n'
/srv/www/stages.resel.fr/env/bin/python manage.py django_cas_ng_clean_sessions
echo '[executed]'