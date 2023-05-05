FROM python:3.7
ENV PYTHONBUFFERED=1
WORKDIR /AITSIDILKHIR
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt  
COPY . .
CMD python manage.py runserver 127.0.0.1:8000


