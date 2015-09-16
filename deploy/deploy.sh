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

if [ -n "$LIVE" ];
then
    echo '--- Running server LIVE'
    supervise .
else
    echo '--- Running server DEVELOPMENT'
    ./manage.py runserver 0.0.0.0:8000
fi
