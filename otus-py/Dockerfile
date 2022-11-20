FROM python:3.9.12-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8000

ENTRYPOINT ["python", "./app.py"]
