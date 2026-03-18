# Base image
FROM python:3.12-slim

# Çalışma dizini
WORKDIR /app

# Kodları kopyala
COPY . /app

# Gerekli bağımlılıkları yükle
RUN pip install --no-cache-dir psutil

# Unbuffered Python
ENV PYTHONUNBUFFERED=1

# Script'i çalıştır
CMD ["python3", "main.py"]
