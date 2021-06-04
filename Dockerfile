FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8
COPY . /app
WORKDIR /app
ENV STATIC_PATH /app/templates/
ENV UWSGI_CHEAPER 4
ENV UWSGI_PROCESSES 64
ENV NGINX_WORKER_PROCESSES auto
RUN echo "uid = root" >> uwsgi.ini
RUN echo "gid = root" >> uwsgi.ini
RUN echo "enable-threads = true" >> uwsgi.ini
RUN echo "ignore-sigpipe=true" >> uwsgi.ini
RUN echo "ignore-write-errors=true" >> uwsgi.ini
RUN echo "disable-write-exception=true" >> uwsgi.ini
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN apk --update add python py-pip openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del build-dependencies

# ENTRYPOINT [ "python" ]
# CMD [ "app.py" ]