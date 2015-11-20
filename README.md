# The Things Network: Frontend Development Environment

Contains thethingsnetwork.org website and the Nodes/Gateways API.

## Setup

  * Install [Docker Toolbox](https://www.docker.com/docker-toolbox)
  * Make sure `docker-machine` is running
  * Build and run all docker containers:

        $ docker-compose build && docker-compose up -d

  * Only first time: run migrations and static files collection 

        $ docker-compose run ttn_org /usr/local/bin/python manage.py migrate
        $ docker-compose run ttn_org /usr/local/bin/python manage.py collectstatic

  * Check the IP address of your docker machine

        $ docker-machine ip <replace-with-your-docker-machine-name>

  * Open your browser and go to the IP address