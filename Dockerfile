FROM python:3.7-slim

WORKDIR /app

COPY . /app

RUN pip install flask flask_login pytz

EXPOSE 5000

CMD ["python", "app.py"]
