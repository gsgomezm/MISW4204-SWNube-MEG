from celery import Celery

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task()
def registrar_log(video, fecha):
    with open('post_txt', 'a+') as file:
        file.write('{} - video posteado: {}\n'.format(video, fecha))