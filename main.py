from flask import Flask
import config
from exts import db, mail, cache, csrf, avatars, jwt, cors
from flask_migrate import Migrate
from models import auth
from blueprints.front import front_bp
from blueprints.media import media_bp
from blueprints.cmsapi import cmsapi_bp
from otaku_celery import make_celery
import commands
#提问：为啥这里不直接写成import exts
#提问：app.route和bp.route什么关系
#提问：import config和app.config.from_object(config)二者选其一就行么，并不,不然括号里的config哪来
#提问：为什么app.config.from_object(config)要写在db.init_app(app)的前面

app = Flask(__name__)#创建 Flask 应用程序实例，并将其存储在名为 app 的变量中。

app.config.from_object(config)#是 Flask 中用于加载配置文件的方法。它将指定的配置对象或模块导入到 Flask 应用程序的配置中
db.init_app(app)#将数据库扩展与应用程序实例进行绑定，以便在应用程序中可以使用数据库扩展提供的功能。
mail.init_app(app)
cache.init_app(app)
csrf.init_app(app)
avatars.init_app(app)
jwt.init_app(app)
cors.init_app(app, resources={r"/cmsapi/*": {"origins": "*"}})
csrf.exempt(cmsapi_bp)

migrate = Migrate(app, db)
otaku_celery = make_celery(app)



#注册蓝图
app.register_blueprint(front_bp)
app.register_blueprint(media_bp)
app.register_blueprint(cmsapi_bp)
#注册命令
app.cli.command("init_boards")(commands.init_boards)
app.cli.command("create_test_posts")(commands.create_test_posts)
app.cli.command("init_roles")(commands.init_roles)
app.cli.command("bind_roles")(commands.bind_roles)
if __name__ == '__main__':

    app.run(debug=True, host="127.0.0.1", port='5000')
    commands.init_boards()


