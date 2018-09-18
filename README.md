

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
    5. python manage.py makemigrations
    6. python manage.py migrate
    7. python manage.py runserver

Currently datahub-be has three datasets, both part of the affordable housing project. To get the data 
for this project got to the Data Wrangling GitHub repository at:

https://github.com/codefordurham/datahub-dw/tree/master/affordablehousing_data

and follow the instructions. You will need to run the datahub_ingest.bin file, which contains a series
of psql command that ingest data into datahub-be.

