from importlib import import_module


def load_config(config_path):
    """自动加载配置"""
    module = import_module(config_path)
    # print(module)
    name = config_path.split('.')[-1]
    if name == 'settings':
        return module.InitConfig
    else:
        return module.Config
