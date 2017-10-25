#!/usr/bin/env bash
cd /srv/www/stages.resel.fr
/srv/www/stages.resel.fr/env/bin/python manage.py clearsessions
/srv/www/stages.resel.fr/env/bin/python manage.py django_cas_ng_clean_sessions 