# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the image
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY .env .
COPY celery_config.py .
COPY db.py .
COPY main.py .
COPY routes.py .
COPY tasks.py .
COPY verification.py .

# Expose port 8002 for the service
EXPOSE 8002

# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002", "--workers", "7"]
