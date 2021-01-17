#!/bin/bash
db_name="$(crudini --get "../config.ini" "database" "database")"
db_user="$(crudini --get "../config.ini" "database" "user")"
db_pass="$(crudini --get "../config.ini" "database" "password")"