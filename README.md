blankspot
=========

**Project not yet running. Keep also care .... learning project of author ;) **

A little tool to collect data of people wanting to contribute to a
location based project like freifunk.

Functions
---------

The software is intended to have this features -- not yet done :

- offering a registration form where people can register with there
  location
- offering a list with geolocation of people registered
- having a backend-interface allowing to get in contact with people

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
logging in as superuser to database and then:

	CREATE DATABASE blankspot;
	CREATE ROLE blankspotuser WITH PASSWORD 'hahahfooo' LOGIN;
	ALTER DATABASE blankspot OWNER TO blankspotuser;

Virtualenv
----------


Install virtualenvwrapper. This can be done either via your packet
manage or by running

	$ pip install virtualenvwrapper

(This HowTo now only describes steps done on a Debian system. When
running Windows or for further detail, check documentation -- a good
idea anyway.)

Now you have to setup your environment.

	$ export WORKON_HOME=~/Envs
	$ mkdir -p $WORKON_HOME
	$ source /usr/local/bin/virtualenvwrapper.sh
	$ mkvirtualenv blankspot

This will create a folder Envs inside your home and install the
virtualenv into it. You might want to add the export and the source
command to your local shell configuration to ensure, it's loaded on
startup.

With running the mkvirtualenv command you will be already inside the
environment. You can install as many environments you wish to and
switch between them by running workon <virutal_env_name>, for example
workon blankspot.

Once inside the virtualenv, you have to install the needed packages.
This can be done by:

	$ pip install -r requirements.txt


License
-------

The software is distributed under terms of AGPL. Please check LICENSE
for details.
