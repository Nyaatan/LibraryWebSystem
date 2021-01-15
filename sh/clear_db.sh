#!/bin/bash
. database.sh

sudo -u postgres -H -- psql <<- SQL
DROP DATABASE IF EXISTS $db_name;
DROP USER IF EXISTS $db_user;
DROP USER IF EXISTS LibraryApp;
SQL
