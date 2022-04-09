FROM python:3

ENV PYTHONUNBUFFERED = 1 \
    MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=password

RUN mkdir /app
WORKDIR /app
RUN pip install --upgrade pip

COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
