FROM python:3.9

MAINTAINER Cropland

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /application
WORKDIR /application
ADD . /application

RUN pip install -r requirements.txt

RUN chmod +x ./entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["sh", "entrypoint.sh"]
