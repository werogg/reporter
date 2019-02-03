#!/usr/bin/env sh

set -u
set -e

cd /code

if [ "${ENVIRON:-dev}" = "dev" ]
then
    pip install --no-cache-dir -r /build/requirements.txt
fi

# Wait for database
echo "Waiting for database"
until nc -z ${DATABASE_HOST} ${DATABASE_PORT}
do
    sleep 1
done
sleep 1

./manage.py migrate --noinput
./manage.py collectstatic --noinput
./manage.py runserver "0.0.0.0:8000"