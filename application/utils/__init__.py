from flask import Blueprint
from importlib import import_module


def path(rule,func_view, **kwargs):
    # 把蓝图下视图和路由之间的映射关系处理成字典结构，方便后面注册蓝图的时候，直接传参
    return {"rule":rule,"view_func":func_view, **kwargs}


def include(url_prefix, blueprint_path):
    """把路由前缀和蓝图进行关系映射"""
    return {"url_prefix":url_prefix,"blueprint_path":blueprint_path}




def init_blueprint(app):
    """自动注册蓝图"""

    blueprint_path_list = app.config.get("INSTALLED_APPS") # ['application.apps.home']

    for i in range(len(blueprint_path_list)):
        if 'application.apps.' not in blueprint_path_list[i]:
            blueprint_path_list[i] = 'application.apps.' + blueprint_path_list[i]
    # print('blueprint_path_list:',blueprint_path_list)

    # 加载admin站点总配置文件
    try:
        import_module(app.config.get("ADMIN_PATH"))
    except:
        pass

    for blueprint_path in blueprint_path_list:
        blueprint_name = blueprint_path.split(".")[-1] # home
        # print(blueprint_name)
        # 自动创建蓝图对象
        # print('blueprint_path：',blueprint_path) # application.apps.home
        blueprint = Blueprint(blueprint_name,blueprint_path) # <flask.blueprints.Blueprint object at 0x7f0055cb7490>
        # print(blueprint)
        # 蓝图自动注册和绑定视图和子路由
        url_module = import_module(blueprint_path + ".urls")  # 加载蓝图下的子路由文件
        for url in url_module.urlpatterns:  # 遍历子路由中的所有路由关系
            blueprint.add_url_rule(**url)  # 注册到蓝图下
        # 读取总路由文件
        url_path = app.config.get("URL_PATH")
        urlpatterns = import_module(url_path).urlpatterns  # 加载蓝图下的子路由文件
        url_prefix = "" # 蓝图路由前缀
        for urlpattern in urlpatterns:
            if urlpattern["blueprint_path"] == blueprint_name+".urls":
                url_prefix = urlpattern["url_prefix"]
                break

        # 注册模型
        import_module(blueprint_path+".models")
        # print(        import_module(blueprint_path+".models"))


        # 加载蓝图内部的admin站点配置
        try:
            import_module(blueprint_path+".admin")
        except:
            pass

        # 加载蓝图内部的socket接口
        try:
            import_module(blueprint_path + ".socket")
        except:
            pass

        # 注册蓝图对象到app应用对象中,  url_prefix 蓝图的路由前缀
        app.register_blueprint(blueprint,url_prefix=url_prefix)


        # # 注册蓝图对象到app应用对象中
        # app.register_blueprint(blueprint,url_prefix="")


















# def init_blueprint(app):
#     """自动注册蓝图"""
#     blueprint_path_list = app.config.get("INSTALLED_APPS") # ['application.apps.home']
#     print(blueprint_path_list)
#     for blueprint_path in blueprint_path_list:
#         blueprint_name = blueprint_path.split(".")[-1] # home
#         print(blueprint_name)
#         # 自动创建蓝图对象
#         print('blueprint_path：',blueprint_path) # application.apps.home
#         blueprint = Blueprint(blueprint_name,blueprint_path) # <flask.blueprints.Blueprint object at 0x7f0055cb7490>
#         print(blueprint)
#         # 蓝图自动注册和绑定视图和子路由
#         url_module = import_module(blueprint_path + ".urls")  # 加载蓝图下的子路由文件
#         for url in url_module.urlpatterns:  # 遍历子路由中的所有路由关系
#             blueprint.add_url_rule(**url)  # 注册到蓝图下
#         # 读取总路由文件
#         url_path = app.config.get("URL_PATH")
#         urlpatterns = import_module(url_path).urlpatterns  # 加载蓝图下的子路由文件
#         url_prefix = "" # 蓝图路由前缀
#         for urlpattern in urlpatterns:
#             if urlpattern["blueprint_path"] == blueprint_name+".urls":
#                 url_prefix = urlpattern["url_prefix"]
#                 break
#
#         # 注册模型
#         import_module(blueprint_path+".models")
#
#         # 注册蓝图对象到app应用对象中,  url_prefix 蓝图的路由前缀
#         app.register_blueprint(blueprint,url_prefix=url_prefix)
#
#
#         # # 注册蓝图对象到app应用对象中
#         # app.register_blueprint(blueprint,url_prefix="")

