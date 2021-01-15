#!/bin/bash
. database.sh

sudo -u postgres -H -- psql <<- SQL
CREATE DATABASE $db_name;
CREATE USER $db_user WITH ENCRYPTED PASSWORD '$db_pass';
GRANT ALL PRIVILEGES ON DATABASE $db_name TO $db_user;
SQL
