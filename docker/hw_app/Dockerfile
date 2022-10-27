FROM python:3.8

COPY hw_app.py /hw_app/hw_app.py

WORKDIR /hw_app

RUN apt-get update && apt-get install -y iputils-ping

CMD ["python", "hw_app.py"]