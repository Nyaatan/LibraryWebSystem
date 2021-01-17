#!/bin/bash
set -e
cd sh
. setup_preq.sh
. setup_db.sh
. setup_db_shema.sh
. setup_db_example.sh
. setup_env.sh