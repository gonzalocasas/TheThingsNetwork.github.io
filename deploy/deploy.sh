#!/usr/bin/env bash

. vars.sh

echo '--- Activating virtualenv'
. $VIRTUAL_ENV/bin/activate

echo '--- Installing missing dependencies'
cd $TTN_ORG/ttn_org
pip3 install -r requirements.txt

echo '--- Migrating, collecting static files'
./manage.py migrate
./manage.py collectstatic

echo '--- Running server'
#TODO webserver
./manage.py runserver 0.0.0.0:80
