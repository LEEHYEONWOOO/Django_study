FROM python:3.10

WORKDIR /app

COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERD 1


RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000 --noreload
