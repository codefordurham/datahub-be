# datahub-be
Back End Service For Data Hub
---
Overview
The datahub-be is a REST service for managing curated data for visualizations.  It's expected to be partnered with datahub-fe, whcih will be the external web interface, but any front end could be used with this.

Planned endpoints (3-7-2017) are:

**GET /health**

Will respond with HEALTHY if the service and it's dependencies are up and running.  Will return UNHEALTHY if the service or any of it's dependencies are down.  Specific dependencies will be called out in the

**POST /projects**

body: {"name":"ABC"}

Create a project space for showing visualizations.  The first space is expected to be "Affordable Housing".

**GET /projects**

Responds with a list of all projects

[{"id":1,"name":"ABC"},{"id":2,"name":"XYZ"}]

**GET /projects/{projectId}**

Responds with a specific project

{"id":2,"name":"XYZ"}

**Getting up and running:**

1. clone this repo
    1. $ `cd ~/codefordurham`
    2. $ `git clone https://github.com/codefordurham/datahub-be.git`
2. set up the postgres db
    1. Install postgresql if you don't already have it.
    2. start server: $`pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start`
    3. create database: $`createdb datahub`
    4. enter db: $`psql datahub`
    5. create table: #`CREATE TABLE projects (id int, name text, mtime timestamp, ctime timestamp);`
3. start up the service
    1. $`cd ~/codefordurham/datahub-be`
    2. $`virtualenv env`
    3. $`source env/bin/activate`
    4. $`pip install -r requirements.txt`
    5. $`python manage.py migrate`
    6. copy/ingest data (see below)
    7. $`python manage.py runserver`

Currently datahub-be has two data sets, both part of the affordable housing project. To get the data for this project clone or download the Data Wrangling GitHub repository at:

https://github.com/codefordurham/datahub-dw/tree/master/durham_propbgs

You can ingest the data by the following SQL commands in the postgresql database:

#`\copy datahub_be_app_propsales FROM '/FULL/PATH/TO/DATASET/propsalescompass_100517.csv' DELIMITER ',' CSV;`

#`\copy datahub_be_app_singfamhouse FROM '/FULL/PATH/TO/DATASET/singfamhouse_100517.csv' DELIMITER ',' CSV;`
