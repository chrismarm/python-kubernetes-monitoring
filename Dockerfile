FROM python:3

WORKDIR /usr/src/app

RUN pip3 install requirements.txt

COPY . .

CMD [ "python3", "monitoring_service.py" ]