FROM python:3.10.2-slim

RUN useradd -ms /bin/bash python

USER  python

WORKDIR /home/Documents/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/Documents/python/app/src

CMD [ "tail", "-f", "/dev/null" ]