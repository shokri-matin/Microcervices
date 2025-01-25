from celery import Celery

app = Celery(
    "powder",
    broker="pyamqp://default_user_ArL_lqp3PYA34scUGPJ:lH65WgtwCceioGeC4ripdGhrwvFeS_Qv@172.22.6.30:30672//",  # Updated RabbitMQ broker URL
    backend="rpc://",
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
