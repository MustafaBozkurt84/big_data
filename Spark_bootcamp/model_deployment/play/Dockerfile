FROM python:3.6
MAINTAINER Erkan SIRIN
#RUN useradd -ms /bin/bash admin
#USER admin

ADD .  /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD [ "python", "app.py" ]