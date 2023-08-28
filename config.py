import os
from datetime import timedelta
SECRET_KEY = "rtyuikl9mnbvcdrt567"

BASE_DIR = os.path.dirname(__file__)

#首先去navicat里创建一个新的数据库
DB_USERNAME = 'root'
DB_PASSWORD = 'malala'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'otakufun'
DB_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS =False

#session.permanent=True的情况下的过期时间,记住我的时间
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
#如果是MAIL_USE_SSL = True, MAIL_PORT = 465
MAIL_USERNAME = '1482775872@qq.com'
MAIL_PASSWORD = 'xrzjebybtrmkjjai'
MAIL_DEFAULT_SENDER = '1482775872@qq.com'

#Celery的redis配置
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
#broker_connection_retry_on_startup = True

#Flask-Caching的配置
CACHE_TYPE = "RedisCache"
CACHE_DEFAULT_TIMEOUT = 300
CACHE_REDIS_HOST = "127.0.0.1"
CACHE_REDIS_PORT = 6379

#配置头像
AVATARS_SAVE_PATH = os.path.join(BASE_DIR, "media", "avatars")

POST_IMAGE_SAVE_PATH = os.path.join(BASE_DIR, "media", "post")

BANNER_SAVE_PATH = os.path.join(BASE_DIR, "media", "banner")
PER_PAGE_COUNT = 10

JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)