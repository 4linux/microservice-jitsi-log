FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine-2020-05-09
COPY ./ /app
RUN pip install -r /app/requirements.txt
