from flask import Flask
from flask_script import Manager
import os, sys

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand   # 导入数据迁移模块，添加数据迁移数据命令模块
from flask_redis import FlaskRedis
from flask_session import Session
from flask_jsonrpc import JSONRPC
from flask_marshmallow import Marshmallow           # 中文译作：棉花糖。是一个轻量级的数据格式转换的模块，也叫序列化和反序列化模块，常用于将复杂的orm模型对象与python原生数据类型之间相互转换。
from flask_jwt_extended import JWTManager
from flask_admin import Admin
from flask_babelex import Babel                        # 是Flask 的翻译扩展工具
from faker import Faker
from flask_pymongo import PyMongo
from flask_qrcode import QRcode
from flask_socketio import SocketIO
from flask_cors import CORS
import pymysql
from application.utils.session import init_session  # 导入加载session加载配置的函数`
from application.utils.logger import Log
from application.utils.commands import load_command
from application.utils import init_blueprint
from application.utils.config import load_config

# from flask_cors import *



# 创建终端脚本管理对象
manager = Manager()

# 创建数据库链接对象
db = SQLAlchemy()
pymysql.install_as_MySQLdb()

# redis 链接对象
redis = FlaskRedis()

# session储存对象
session_store = Session()

# 数据迁移实例化模块
migrate = Migrate()

# 日志对象
log = Log()

# 初始化json_rpc模块
json_rpc = JSONRPC()

# 数据转换器的对象创建
ma = Marshmallow()

# jwt认证模块实例化
jwt = JWTManager()

# flask-admin模块初始化
admin = Admin()

# flask_babelex模块初始化
babel = Babel()

# flask_PyMongo模块初始化
mongo = PyMongo()

# flask_qrcode模块实例化
qrcode = QRcode()

# flask_socketio模块实例化
SocketIO = SocketIO()

# flask_cors模块实例化
cors = CORS()

#  style="border-radius:50%"
def init_app(config_path):
    """全局初始化"""
    # 创建app应用对象
    app = Flask(__name__)
    # 项目根目录
    # 　os.path.dirname　功能：去掉文件名，返回目录
    app.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # /home/yanmu/桌面/mofang/mofangapi

    # 加载导包路径
    sys.path.insert(0, os.path.join(app.BASE_DIR, "application/utils/language"))

    # 加载配置
    Config = load_config(config_path)
    app.config.from_object(Config)

    # 数据库初始化
    db.init_app(app)
    app.db = db
    redis.init_app(app)
    mongo.init_app(app)

    # 数据转换器的初始化
    ma.init_app(app)

    # session储存初始化
    init_session(app)
    session_store.init_app(app)

    # 数据化迁移初始化
    migrate.init_app(app, db)

    # 添加数据迁移的命令到终端脚本工具中
    manager.add_command('db',MigrateCommand)

    # 日志初始化
    app.log = log.init_app(app)

    # 蓝图注册
    init_blueprint(app)

    # 初始化json_rpc
    json_rpc.service_url = "/api"  # api接口的url地址前缀
    json_rpc.init_app(app)

    # jwt初始化
    jwt.init_app(app)



    # 国际化本地化模块的初始化
    babel.init_app(app)

    # 初始化终端脚本工具
    manager.app = app

    # 数据种子生成器[faker]
    app.faker = Faker(app.config.get("LANGUAGE"))

    # qrcode初始化配置
    qrcode.init_app(app)

    # cors初始化配置
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    # socketio
    SocketIO.init_app(app, cors_allowed_origins=app.config["CORS_ALLOWED_ORIGINS"], async_mode=app.config["ASYNC_MODE"], debug=app.config["DEBUG"])
    # 改写runserver命令
    if sys.argv[1] == "runserver":
        manager.add_command("run", SocketIO.run(app,host=app.config["HOST"],port=app.config["PORT"]))
    # 注册自定义命令
    load_command(manager)

    # admin站点
    from flask_admin import AdminIndexView
    admin.init_app(app)

    # 项目语言
    babel.init_app(app)



    return manager
