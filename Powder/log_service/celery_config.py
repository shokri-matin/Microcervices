import os
from celery import Celery

RABBITMQ_ADDR = os.getenv("RABBITMQ_ADDR", "unknown_service")

app = Celery(
    "powder",
    broker=RABBITMQ_ADDR,  # Updated RabbitMQ broker URL
    backend="rpc://",
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
