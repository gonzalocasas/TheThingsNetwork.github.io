#!/usr/bin/env bash

# Public variables (no passwords!)

export VIRTUAL_ENV=~/.venv
export TTN_ORG=~/ttn_org

if [ -e "$HOME/local_vars.sh" ]; then
    . "$HOME/local_vars.sh"  # put local secrets here
fi
