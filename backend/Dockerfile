FROM python:3.6

WORKDIR /code
RUN mkdir -p /code/src
COPY requirements.txt .
COPY src/manage.py /code/src/manage.py

RUN pip install -r requirements.txt

COPY src /code/src

EXPOSE 8000
