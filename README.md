# The Things Network: Frontend Development Environment

Contains thethingsnetwork.org website and the Nodes/Gateways API (MongoDB).

## Setup

  * Install [Docker Toolbox](https://www.docker.com/docker-toolbox)
  * Make sure `docker-machine` is running
  * Clone the `server-devenv` repository on the same level as this repository

        $ git clone git@github.com:TheThingsNetwork/server-devenv.git

  * Build and run all docker containers:

        $ docker-compose build && docker-compose up -d

  * Only first time: run migrations and static files collection 

        $ docker-compose run ttn_org /usr/local/bin/python manage.py migrate
        $ docker-compose run ttn_org /usr/local/bin/python manage.py collectstatic

  * Check the IP address of your docker machine

        $ docker-machine ip <replace-with-your-docker-machine-name>

  * Open your browser and go to the IP address