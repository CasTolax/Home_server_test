# Base image
FROM python:3.12-slim

# working directory
WORKDIR /app

# copy codes
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir psutil

# Unbuffered Python
ENV PYTHONUNBUFFERED=1

# start the script
CMD ["python3", "main.py"]
