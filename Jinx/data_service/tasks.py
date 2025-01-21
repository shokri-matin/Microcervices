from celery_config import app as celery_app

@celery_app.task(name='tasks.log_task')
def log_task(metadata):
    """
    Submit a task to log_service to logging everything!
    """
    celery_app.send_task(
        "tasks.log_task"
        , args=[metadata],
        queue="default")