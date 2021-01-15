#!/bin/bash
. database.sh

sudo -u postgres -H -- psql -d $db_name  < ../sql/create_schema.sql
