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
    1. cd ~/codefordurham
    2. clone https://github.com/codefordurham/datahub-be.git
2. set up the postgres db
    1. start server: pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
    2. create database: createdb datahub
    3. enter db: psql datahub
    4. CREATE TABLE IF NOT EXISTS projects (id int, name text, mtime timestamp, ctime timestamp);
3. Ensure [GDAL](https://www.gdal.org/ "GDAL") is installed.
4. start up the service
    1. cd ~/codefordurham/datahub-be
    2. If you use [pipenv](https://github.com/pypa/pipenv "pipenv") - `pipenv install . -e`
    3. virtualenv env
    4. source env/bin/activate
    5. pip install -r requirements.txt
    6. python manage.py makemigrations
    7. python manage.py migrate
    8. python manage.py runserver

Currently datahub-be has three datasets, both part of the affordable housing project. To get the data
for this project got to the Data Wrangling GitHub repository at:

https://github.com/codefordurham/datahub-dw/tree/master/affordablehousing_data

and follow the instructions. You will need to run the datahub_ingest.bin file, which contains a series
of psql command that ingest data into datahub-be.
