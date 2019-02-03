#!/usr/bin/env bash

SUPERUSER_ENVIRONMENTS="dev test"
PG_SUPERUSER="NOSUPERUSER"
test -n "${ENVIRON}" \
    && (echo $SUPERUSER_ENVIRONMENTS | grep -q "${ENVIRON}") \
    && PG_SUPERUSER="SUPERUSER"

echo "Creating ${DATABASE_NAME} in environment (${ENVIRON}) with ${PG_SUPERUSER}"
psql -c "CREATE USER ${DATABASE_USER} CREATEDB ${PG_SUPERUSER} NOCREATEROLE INHERIT LOGIN PASSWORD '${DATABASE_PASS}';"
createdb --owner ${DATABASE_USER} --template template0 --encoding=UTF8 --lc-ctype=en_US.UTF-8 --lc-collate=en_US.UTF-8 ${DATABASE_NAME};