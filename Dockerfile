FROM python:3.8
LABEL MAINTAINER="Taha Mousavi|TahaM8000@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir /Weblog
WORKDIR /Weblog

COPY . /Weblog


ADD requirements.txt /Weblog
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi"]
