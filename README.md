blankspot
=========

A little tool to collect data of people wanting to contribute to a
location based project like freifunk.

Dependencies
------------

Blankspot depends on:

- Django and therefor Python
- A database server supported by django (PostgreSQL recommended) and
  its development libraries -- we have used PostgreSQL here

For detailed list of python dependencies, have a look at
requirements.txt next to this file.


Creating databaseuser
---------------------

Having default settings on settings.py you will need to run a postgres
server on localhost. Needed user and database can be create e.g. with
logging in as superuser to database and than:

	CREATE DATABSE blankspot;
	CREATE ROLE blankspotuser WITH PASSWORD 'hahahfooo' LOGIN;
	ALTER DATABASE blankspot OWNER TO blankspotuser;
