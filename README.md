# datahub-be
Back End Service For Data Hub
---
Overview
The datahub-be is a REST service for managing curated data for visualizations.  It's expected to be partnered with datahub-fe, whcih will be the external web interface, but any front end could be used with this.

Planned endpoints (3-7-2017) are:

**GET /health**

Will respond with HEALTHY if the service and it's dependencies are up and running.  Will return UNHEALTHY if the service or any of it's dependencies are down.  Specific dependencies will be called out in the 

**POST /project**

body: {"name":"ABC"}

Create a project space for showing visualizations.  The first space is expected to be "Affordable Housing".

**Getting up and running:**

1. clone this repo
    1. cd ~/codefordurham
    2. clone https://github.com/codefordurham/datahub-be.git
2. set up the postgres db
    1. start server: pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
    2. create database: createdb datahub
    3. enter db: psql datahub
    4. CREATE TABLE IF NOT EXISTS projects (id int, name text, mtime timestamp, ctime timestamp);
3. start up the service
    1. cd ~/codefordurham/datahub-be
    2. virtualenv env
    3. source env/bin/activate
    4. pip install -r requirements.txt
    5. python manage.py migrate
    6. python manage.py runserver
