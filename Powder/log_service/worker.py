from loguru import logger

from celery_config import app as celery_app

# Configure the log file
logger.remove()
logger.add(
    "logs/app.json",
    format='{{"timestamp": "{time}", "level": "{level}", "service": "log_service", "message": "{message}"}}',
    rotation="10 MB",
    retention="7 days",
    level="INFO",
    serialize=True,
)

@celery_app.task(name="tasks.log_task")
def store_log(metadata):
    """Process and store log messages with metadata."""
    log_message = metadata.get("log_message", "")
    service_name = metadata.get("service_name", "unknown_service")
    log_level = metadata.get("log_level", "INFO")
    client_ip = metadata.get("client_ip", "unknown_ip")
    user_id = metadata.get("user_id", "unknown_user")

    logger.info(
        f"Service: {service_name} | User: {user_id} | IP: {client_ip} | Log: {log_message}",
        level=log_level,
    )
