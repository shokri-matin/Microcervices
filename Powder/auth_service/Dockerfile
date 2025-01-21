# Use a lightweight image with Python 3.9
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary application files to the working directory
COPY .env .
COPY main.py .  
COPY requirements.txt .  
COPY authentication ./authentication
COPY database ./database
COPY models ./models
COPY routes ./routes

# Install the required Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8001 for the service
EXPOSE 8001

# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--workers", "7"]
