FROM authservice:latest

# Copy the necessary application files to the working directory
COPY . .

# Expose port 8001 for the service
EXPOSE 8001

# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8001", "--workers", "7"]
