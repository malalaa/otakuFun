from exts import db
import shortuuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin


class Permission(object):
    # 255的二进制方式来表示 1111 1111
    ALL_PERMISSION = 0b11111111
    # 1. 访问者权限
    VISITOR =        0b00000001
    # 2. 管理帖子权限
    POST =         0b00000010
    # 3. 管理评论的权限
    COMMENT =      0b00000100
    # 4. 管理板块的权限
    BANNER =        0b00001000
    # 5. 管理前台用户的权限
    USER =      0b00010000
    # 6. 管理后台管理员的权限
    STAFF =        0b01000000


class RoleModel(db.Model, SerializerMixin):
    serialize_only = ("id", "name", "desc", "create_time")
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(200),nullable=True)
    create_time = db.Column(db.DateTime,default=datetime.now)
    permissions = db.Column(db.Integer,default=Permission.VISITOR)




class UserModel(db.Model, SerializerMixin):
    serialize_rules = ("-_password", "-posts", "-comments" )
    #serialize_only = ("id", "email", "username", "avatar", "signature", "join_time", "is_staff", "is_active")
    __tablename__ = "user"
    #autoincrement=True 生成短型 UUID（Universally Unique Identifier，通用唯一标识符）的 Python 库
    #并不具备自增长的功能，因为 UUID 是设计为在分布式系统中保持唯一性而不是顺序增长的
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)  # 练习的时候这里是自增长，注意现在不是了
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    _password = db.Column(db.String(200), nullable=False)
    # realname = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(100))
    signature = db.Column(db.String(100))
    join_time = db.Column(db.DateTime, default=datetime.now)
    # 权限
    is_staff = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    role = db.relationship("RoleModel", backref="users")


    def __init__(self, *args, **kwargs):  # 万能参数，前者代表一切未知参数，后者代表关键字参数x=12
        if "password" in kwargs:
            self.password = kwargs.get('password')
            kwargs.pop('password')
        super(UserModel, self).__init__(*args, **kwargs)  # super() 调用父类的 __init__ 方法


    @property  # 这是一个装饰器，用于将一个方法转换为属性访问器，可以通过属性方式访问函数
    def password(self):  # 访问
        return self._password


    @password.setter  # 赋值
    def password(self, newpwd):  # user.password = newpwd
        self._password = generate_password_hash(newpwd)

    def check_password(self, rawpwd):
        return check_password_hash(self.password, rawpwd)

    def has_permission(self, permission):
        return (self.role.permissions & permission) == permission
