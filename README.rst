
Modi Features
=============

Requires::

  postgresql >= 9.1
  postgis    >= 2.0
  python     >= 2.7

Install::

  $ createdb modifeatures
  $ psql -d modifeatures -f ddl.sql

  # make virtual env 
  (env)$ python setup.py develop
  (env)$ paster serve development.ini --reload
