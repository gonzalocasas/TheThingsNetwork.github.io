#!/usr/bin/env bash

# Public variables (no passwords!)

export VIRTUAL_ENV=~/.venv
export TTN_ORG=~/ttn_org

export API_INFLUX_HOST="croft.thethings.girovito.nl"
export API_INFLUX_PORT="8086"
export API_INFLUX_DB="jolie"
export API_MONGO_HOST="croft.thethings.girovito.nl"
export API_MONGO_PORT="27017"
export API_MONGO_DB="jolie"

if [ -e "$HOME/local_vars.sh" ]; then
    . "$HOME/local_vars.sh"  # put local secrets here
fi
