# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the image
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY celery_config.py .
COPY worker.py .
COPY logs ./logs

# Start the Celery worker
CMD ["celery", "-A", "worker.celery_app", "worker", "--loglevel=info"]
