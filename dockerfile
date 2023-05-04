FROM python:3.7
ENV PYTHONBUFFERED=1
WORKDIR /django
COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt  
COPY . .
CMD python manage.py runserver 0.0.0.0:8000


