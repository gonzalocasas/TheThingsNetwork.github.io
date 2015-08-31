#!/usr/bin/env bash

# Install VM necessary to host TTN public website.
# Author: Martijn van der Veen
# TODO: port to Docker container script

. vars.sh

sudo apt-get install python3-pip python3-virtualenv virtualenv nginx daemontools

cd ~
git clone https://github.com/TheThingsNetwork/TheThingsNetwork.github.io.git $TTN_ORG
if [ ! -d "$VIRTUAL_ENV" ]; then
    virtualenv $VIRTUAL_ENV -p python3
fi
. $VIRTUAL_ENV/bin/activate

