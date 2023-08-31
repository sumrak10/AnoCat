#!/bin/bash
set -e


psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE DATABASE $DB__NAME;
	CREATE USER $DB__USER WITH PASSWORD '$DB__PASS';
	GRANT ALL PRIVILEGES ON DATABASE $DB__NAME TO $DB__USER;
EOSQL