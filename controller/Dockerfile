FROM skiftcreative/gunicorn:latest

WORKDIR /app

COPY . /app

RUN pip3 install -U -r /app/requirements.txt

# uncomment to use your own supervisord.conf
# COPY supervisord.conf /etc/supervisord.conf

# if you need your own gunicorn_conf.py, uncomment this line
# COPY gunicorn_config.py /deploy/

EXPOSE 8000

CMD ["gunicorn", "hello-world-controller:__hug_wsgi__"]

