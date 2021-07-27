#!/usr/bin/sh

nginx

su - celery -c "export ENV=$ENV &&\
                cd /var/www/html/pages &&\
                python manage.py collectstatic --noinput &&\
                python manage.py makemigrations &&\
                python manage.py migrate &&\
                python manage.py loaddata  nb.json &&\
                uwsgi --ini uwsgi.ini"

su - celery -c 'cd /var/www/html/pages && nohup celery -A pages worker -l info &> /tmp/celery-worker.log &'
su - celery -c 'cd /var/www/html/pages && nohup celery -A pages beat -l info &> /tmp/celery-beat.log &'

sleep 20

tail -f /tmp/pages-master.log
