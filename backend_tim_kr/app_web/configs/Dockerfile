FROM python:3.8

WORKDIR /opt/app

COPY app_web/configs/requirements.txt .

RUN pip3 install -r /opt/app/requirements.txt

COPY ./app_web .

CMD sleep 10 && python3 manage.py