#!/usr/bin/env bash

cd `dirname $0`
. vars.sh

echo '--- Activating virtualenv'
. $VIRTUAL_ENV/bin/activate

echo '--- Installing missing dependencies'
cd $TTN_ORG/ttn_org
pip3 install -r requirements.txt

echo '--- Migrating, collecting static files'
./manage.py migrate
./manage.py collectstatic --noinput --link --clear

echo '--- Running server'
#./manage.py runserver 0.0.0.0:80
supervise .
