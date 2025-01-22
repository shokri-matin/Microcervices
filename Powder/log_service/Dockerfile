FROM logservice:latest
# Copy the application code
COPY . .

# Start the Celery worker
CMD ["celery", "-A", "worker.celery_app", "worker", "--loglevel=info"]
