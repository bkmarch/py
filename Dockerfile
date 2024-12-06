FROM python:3.13

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ADD manage.py .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#docker build -t compapp .
#docker run --publish 8000:8000 compapp