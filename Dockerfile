FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate

EXPOSE 8003

CMD ["python", "manage.py", "runserver", "0.0.0.0:8003"]