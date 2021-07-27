FROM gssjl2008/django-py3-nginx-alpine:latest

# 标签说明
# docker rmi  pages:v1 || echo "not" && docker build -t pages:v1 -f Dockerfile_pages .
LABEL author="gssjl2008" email="gssjl2004@126.com" desc="python3.8+nginx+uwsgi+Django3镜像，用于pages项目"


RUN  mkdir -p /var/www/html && \
    sed -i '5i\pid  /tmp/nginx.pid;' /etc/nginx/nginx.conf

# 添加项目
ADD . /var/www/html/pages
ADD nginx.conf /etc/nginx/conf.d/django.conf

EXPOSE 80

WORKDIR /var/www/html/pages

RUN pip install -r requirements.txt && \
    chmod u+x start.sh && \
    addgroup -S celery && adduser -S -G celery -s /bin/ash celery && \
    echo -e 'celery\ncelery' | passwd celery && \
    chown -R celery.celery /var/www/html/pages

CMD ["sh", "start.sh"]
