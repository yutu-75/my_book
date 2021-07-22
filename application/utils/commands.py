
import os
from flask_script import Command, Option
from importlib import import_module  # 导入一个模块或者包的函数
import inspect                       # 检查对象


def load_command(manager, command_path=None):
    """自动加载自定义终端命令"""
    if command_path is None:
        command_path = 'application.utils.commands'

    module = import_module(command_path)
    # <module 'application.utils.commands' from '/home/yanmu/桌面/mofang/mofangapi/application/utils/commands.py'>
    # import_module 有两个参数 name 和  package
    #  name 指定了以绝对或相对导入方式导入什么模块
    # 如果参数 name 使用相对导入的方式来指定，那么那个参数 packages 必须设置为那个包名，这个包名作为解析这个包名的锚点 (比如 import_module('..mod', 'pkg.subpkg') 将会导入 pkg.mod)。
    # print('module:%s'% module) # module:<module 'application.utils.commands' from '/home/yanmu/桌面/mofang/mofangapi/application/utils/commands.py'>
    # print('inspect.isclass:%s'% inspect.isclass) # inspect.isclass:<function isclass at 0x7f55c20ab430>

    class_list = inspect.getmembers(module,inspect.isclass)
    # inspect.getmembers( 参数名称到相应Parameter对象的有序映射 。参数以严格的定义顺序出现，包括仅关键字参数。
    # inspect.isclass 返回True对象是否为类，无论是内置的还是用Python代码创建的。
    # print(class_list) # [('BlueprintCommand', <class 'application.utils.commands.BlueprintCommand'>), ('Command', <class 'flask_script.commands.Command'>), ('Option', <class 'flask_script.commands.Option'>)]

    for class_item in class_list:
        if issubclass(class_item[1],Command) and class_item[0] != "Command":
            manager.add_command(class_item[1].name,class_item[1])
class BlueprintCommand(Command):
    """蓝图生成命令"""
    name = "blue"
    option_list = [
        Option('--name','-n',dest='name'),
    ]

    def run(self,name):
        # 生成蓝图名称对象目录
        os.mkdir(name)
        open('%s/__init__.py' % name, 'w')
        open('%s/views.py' % name, 'w')
        open('%s/models.py' % name, 'w')
        with open('%s/urls.py' % name, 'w') as f:
            content = """from . import views
from application.utils import path 
urlpatterns = [

]           
"""
            f.write(content)
        print('蓝图%s创建完成....' % name)





from flask import current_app
import random
from faker.providers import internet
class CreateUserCommand(Command):
    """生成自定义数量的用户信息"""
    name = "faker"
    option_list = [
        Option('--num', '-n', dest='num'),
    ]
    def run(self, num):
        with current_app.app_context():
            from application.apps.users.models import User,UserProfile
            current_app.faker.add_provider(internet)
            faker = current_app.faker

            try:
                num = int(num)
            except:
                num = 1
            user_list = []
            password = "123456"
            for _ in range(0,num):
                sex = bool( random.randint(0,2) )
                if sex == 0:
                    # 性别保密的用户
                    nickname = faker.name()
                elif sex == 1:
                    # 性别为男的用户
                    nickname = faker.name_male()
                else:
                    # 性别为女的用户
                    nickname = faker.name_female()
                name = faker.pystr(min_chars=6, max_chars=16)
                # 生成指定范围的时间对象
                age = random.randint(13,50)
                birthday = faker.date_time_between(start_date="-%sy" % age, end_date="-12y", tzinfo=None)
                hometown_province = faker.province()
                hometown_city = faker.city()
                hometown_area = faker.district()
                living_province = faker.province()
                living_city = faker.city()
                living_area = faker.district()

                user = User(
                    nickname=nickname,
                    sex=sex,
                    name=name,
                    password=name,
                    money=random.randint(100,99999),
                    ip_address=faker.ipv4_public(),
                    email=faker.ascii_free_email(),
                    mobile=faker.phone_number(),
                    unique_id=faker.uuid4(),
                    province=faker.province(),
                    city=faker.city(),
                    area=faker.district(),
                    info=UserProfile(
                        birthday=birthday,
                        hometown_province=hometown_province,
                        hometown_city=hometown_city,
                        hometown_area=hometown_area,
                        hometown_address=hometown_province+hometown_city+hometown_area+faker.street_address(),
                        living_province=living_province,
                        living_city=living_city,
                        living_area=living_area,
                        living_address=living_province+living_city+living_area+faker.street_address()
                    )
                )

                user_list.append(user)

            current_app.db.session.add_all(user_list)
            current_app.db.session.commit()