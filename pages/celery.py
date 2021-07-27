import os
from celery import Celery

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pages.settings.base')

# 实例
app = Celery('pages')

# namespace='CELERY'作用是允许你在Django配置文件中对Celery进行配置
# 但所有Celery配置项必须以CELERY开头，防止冲突
app.config_from_object('django.conf:settings', namespace='CELERY')


# 自动发现django的已注册的任务
app.autodiscover_tasks()

#
# # demo
# @app.task(bind=True)
# def debug_task(self):
#     print(f"Request: {self.request1!r}")