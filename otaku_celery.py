from flask_mail import Message  # 发送邮件就必须构建一个Message类
from exts import mail
from celery import Celery


def send_mail(recipient, subject, body):
    message = Message(subject=subject, recipients=[recipient], body=body)
    try:
        mail.send(message)
        return {"status": "SUCCESS"}
    except Exception:
        return {"status": "FAILURE"}


# 创建celery对象工厂函数
def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    app.celery = celery #将创建好的 Celery 实例绑定到 Flask 应用实例上，这样在其他地方可以通过 app.celery 来访问 Celery 实例
    # 添加任务
    celery.task(name="send_mail")(send_mail)
    return celery
