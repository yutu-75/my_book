import pymongo

"""数据库连接"""

# # 无密码连接

# # 数据库链接，必须保证当前系统能正常访问mongodb！！!
# connect = pymongo.MongoClient('mongodb://127.0.0.1:27017')
# # 创建/切换数据库，数据库不存在则会库中有文档以后，自动创建
# my_db = connect["mofang"]
# print(my_db) # 数据库信息
# # Database(MongoClient(host=['127.0.0.1:27017'], document_class=dict, tz_aware=False, connect=True), 'mofang')
#
# # 创建/进入集合，集合不存在则会集合中有文档以后，自动创建
# my_collections = my_db["my_collections"]
# print(my_collections) # 集合信息
# # Collection(Database(MongoClient(host=['127.0.0.1:27017'], document_class=dict, tz_aware=False, connect=True), 'mofang'), 'my_collections')


# # 有密码连接

"""方式1：如果账号密码没有特殊字符"""
# from pymongo import MongoClient
# connect = MongoClient("mongodb://mofang:123@127.0.0.1:27017/mofang")
# my_db = connect['mofang']                             # 创建/切换数据库
# my_collections = my_db["my_collections"]              # 创建/进入集合
# data = {"name":'nasa',"sex":True,'age':16}            # 参数
# ret = my_collections.insert_one(data)                 # 添加参数
# print(ret.inserted_id)  # 5fd21cc92b280a7470998b7e    # 返回的id值


"""方式2：当前当前库的管理员链接"""
# from pymongo import MongoClient
# from urllib import parse
# username = parse.quote_plus('mofang')                 # 对用户名进行编码
# password = parse.quote_plus('123')                    # 对密码进行编码
# database = parse.quote_plus('mofang')                 # 对密码进行编码
# connect = MongoClient("mongodb://{}:{}@127.0.0.1:27017/{}".format(username,password,database))
# my_db = connect['mofang']                             # 创建/切换数据库
# my_collections = my_db["my_collections"]              # 创建/进入集合
# data = {"name":'yeqi',"sex":False,'age':15}           # 参数
# ret = my_collections.insert_one(data)                 # 添加参数
# print(ret.inserted_id)  # 5fd21f267ae8ccfad62e7743    # 返回的id值


# """方式3: 基于超级管理员身份链接。不需要当前库的管理员了"""
from pymongo import MongoClient

# from urllib import parse
# username = parse.quote_plus('root')                   # 对用户名进行编码
# password = parse.quote_plus('123')                      # 对密码进行编码
# database = parse.quote_plus('admin')                   # 对密码进行编码
# host = "127.0.0.1"                                      # 服务器ip地址
# port = '27017'                                          # 端口号
# connect = pymongo.MongoClient('mongodb://{}:{}@{}:{}/{}'.format(username,password,host,port,database))
# my_db = connect['mofang']                               # 创建/切换数据库
# my_collections = my_db["my_collections"]                # 创建/进入集合
# data = {"name":'樱满集',"sex":True,'age':16}             # 参数
# ret = my_collections.insert_one(data)                   # 添加参数
# print(ret.inserted_id)  # 5fd2230ff92b583773a1c8e3      # 返回的id值


"""集合与数据库管理"""

# from pymongo import MongoClient
# connect = MongoClient("mongodb://root:123@127.0.0.1:27017/admin")
# my_db = connect["mofang"]                               # 创建/进入数据库
# my_collections = my_db["my_collections"]                # 创建/进入集合
# # 查看所有数据库[除了三个基本数据库以外，其他数据库只会显示有文档数据的]
# ret = connect.list_database_names()
# print(ret)           # 查询所有的数据库                    # ['admin', 'config', 'local', 'mofang', 'mogang']
# ret1 = my_db.list_collection_names()
# print(ret1)           # 查询当前数据库的collections集合     # ['my_collections']
#
# # 删除集合的方式1
# my_collections_delete = my_db["notify_list"]
# # my_collections_delete.drop()
#
# # 删除集合的方式2
# my_db.drop_collection("notify_list")


"""mongo添加文档"""

# from pymongo import MongoClient
#
# connect = MongoClient("mongodb://root:123@127.0.0.1:27017/admin")
# my_db = connect["mofang"]  # 创建/进入数据库
# my_collections = my_db["my_collections"]  # 创建/进入集合
# 添加一条数据
# document = {"name":"佐藤优一","mobile":"15025555666","age":17,"sex":False}
# ret = my_collections.insert_one(document)
# print(ret.inserted_id)   # 返回主键ID           5fd22ca7a274c48b793f14b4
#
# 添加多条数据
#
# data_list = [
#     {"name": "罪恶王冠_恙神涯", "mobile": "574158", "age": 23, "sex": False},
#     {"name": "罪恶王冠_樱满集", "mobile": "777777", "age": 17, "sex": False},
#     {"name": "罪恶王冠_楪祈", "mobile": "111111", "age": 16, "sex": True},
#     {"name": "Charlotte_乙坂有宇", "mobile": "123456", "age": 17, "sex": False},
#     {"name": "Charlotte_友利奈绪", "mobile": "654321", "age": 16, "sex": True},
#     {"name": "Charlotte_黑羽美砂", "mobile": "999999", "age": 18, "sex": True},
# ]
# ret = my_collections.insert_many(data_list)
# print(ret.inserted_ids)
# 返回每一条数据主键ID
# [ObjectId('5fd22d1969cd7dcfb865d258'), ObjectId('5fd22d1969cd7dcfb865d259'), ObjectId('5fd22d1969cd7dcfb865d25a'), ObjectId('5fd22d1969cd7dcfb865d25b'), ObjectId('5fd22d1969cd7dcfb865d25c'), ObjectId('5fd22d1969cd7dcfb865d25d')]





"""查询文档(集合 collections)"""


from pymongo import MongoClient

connect = MongoClient("mongodb://root:123@127.0.0.1:27017/admin")
my_db = connect["mofang"]  # 创建/进入数据库
my_collections = my_db["my_collections"]  # 创建/进入集合

"""获取一条"""
# document = my_collections.find_one()
# print(document)
# # {'_id': ObjectId('5fd21cc92b280a7470998b7e'), 'name': 'nasa', 'sex': True, 'age': 16}
# # 获取数据中的信息
# print(document["name"])         # nasa

"""获取多条数据"""
# document_list = my_collections.find()
# print(document_list)        # <pymongo.cursor.Cursor object at 0x7f7aaf9b16d0>
# for document in document_list:
#     print(document)
#     print(document["name"])

"""

{'_id': ObjectId('5fd21cc92b280a7470998b7e'), 'name': 'nasa', 'sex': True, 'age': 16}
nasa
{'_id': ObjectId('5fd21f0b722ca8317cddcc5c'), 'name': 'yeqi', 'sex': False, 'age': 15}
yeqi
{'_id': ObjectId('5fd21f267ae8ccfad62e7743'), 'name': 'yeqi', 'sex': False, 'age': 15}
yeqi
{'_id': ObjectId('5fd2206c81970531b2750b6b'), 'name': '樱满集', 'sex': True, 'age': 16}
樱满集
{'_id': ObjectId('5fd2230ff92b583773a1c8e3'), 'name': '樱满集', 'sex': True, 'age': 16}
樱满集
{'_id': ObjectId('5fd2231e58d8b8fe3b10c1d4'), 'name': '樱满集', 'sex': True, 'age': 16}
樱满集
{'_id': ObjectId('5fd22ca7a274c48b793f14b4'), 'name': '佐藤优一', 'mobile': '15025555666', 'age': 17, 'sex': False}
佐藤优一
{'_id': ObjectId('5fd22d1969cd7dcfb865d258'), 'name': '罪恶王冠_恙神涯', 'mobile': '574158', 'age': 23, 'sex': False}
罪恶王冠_恙神涯
{'_id': ObjectId('5fd22d1969cd7dcfb865d259'), 'name': '罪恶王冠_樱满集', 'mobile': '777777', 'age': 17, 'sex': False}
罪恶王冠_樱满集
{'_id': ObjectId('5fd22d1969cd7dcfb865d25a'), 'name': '罪恶王冠_楪祈', 'mobile': '111111', 'age': 16, 'sex': True}
罪恶王冠_楪祈
{'_id': ObjectId('5fd22d1969cd7dcfb865d25b'), 'name': 'Charlotte_乙坂有宇', 'mobile': '123456', 'age': 17, 'sex': False}
Charlotte_乙坂有宇
{'_id': ObjectId('5fd22d1969cd7dcfb865d25c'), 'name': 'Charlotte_友利奈绪', 'mobile': '654321', 'age': 16, 'sex': True}
Charlotte_友利奈绪
{'_id': ObjectId('5fd22d1969cd7dcfb865d25d'), 'name': 'Charlotte_黑羽美砂', 'mobile': '999999', 'age': 18, 'sex': True}
Charlotte_黑羽美砂

"""



"""字段投影：只显示部分字段，1表示显示，0表示隐藏"""
# document_list = my_collections.find({},{"name":1,"_id":0})
# for document in document_list:
#     print(document)

"""
{'name': 'nasa'}
{'name': 'yeqi'}
{'name': 'yeqi'}
{'name': '樱满集'}
{'name': '樱满集'}
{'name': '樱满集'}
{'name': '佐藤优一'}
{'name': '罪恶王冠_恙神涯'}
{'name': '罪恶王冠_樱满集'}
{'name': '罪恶王冠_楪祈'}
{'name': 'Charlotte_乙坂有宇'}
{'name': 'Charlotte_友利奈绪'}
{'name': 'Charlotte_黑羽美砂'}
"""


"""基于查询条件获取数据"""

# 值相等
# query = {"name":{"$eq":"樱满集"}}
# document = my_collections.find_one(query)  #
# print(document) # {'_id': ObjectId('5fd2206c81970531b2750b6b'), 'name': '樱满集', 'sex': True, 'age': 16}
#
# # 查询方式一样 下面简单
# query1 = {"name":"xiaoming"}
# document = my_collections.find_one(query1)  #
# print(document) # {'_id': ObjectId('5fd2206c81970531b2750b6b'), 'name': '樱满集', 'sex': True, 'age': 16}




# query = {"age":{"$gt":17}}          # age  >  17
# {'_id': ObjectId('5fd22d1969cd7dcfb865d258'), 'name': '罪恶王冠_恙神涯', 'mobile': '574158', 'age': 23, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25d'), 'name': 'Charlotte_黑羽美砂', 'mobile': '999999', 'age': 18, 'sex': True}

# query = {"age":{"$gte":17}}       # age >= 17
# {'_id': ObjectId('5fd22ca7a274c48b793f14b4'), 'name': '佐藤优一', 'mobile': '15025555666', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d258'), 'name': '罪恶王冠_恙神涯', 'mobile': '574158', 'age': 23, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d259'), 'name': '罪恶王冠_樱满集', 'mobile': '777777', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25b'), 'name': 'Charlotte_乙坂有宇', 'mobile': '123456', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25d'), 'name': 'Charlotte_黑羽美砂', 'mobile': '999999', 'age': 18, 'sex': True}

# query = {"age":{"$lte":17}}       # age <= 17
# {'_id': ObjectId('5fd21cc92b280a7470998b7e'), 'name': 'nasa', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd21f0b722ca8317cddcc5c'), 'name': 'yeqi', 'sex': False, 'age': 15}
# {'_id': ObjectId('5fd21f267ae8ccfad62e7743'), 'name': 'yeqi', 'sex': False, 'age': 15}
# {'_id': ObjectId('5fd2206c81970531b2750b6b'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2230ff92b583773a1c8e3'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2231e58d8b8fe3b10c1d4'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd22ca7a274c48b793f14b4'), 'name': '佐藤优一', 'mobile': '15025555666', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d259'), 'name': '罪恶王冠_樱满集', 'mobile': '777777', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25a'), 'name': '罪恶王冠_楪祈', 'mobile': '111111', 'age': 16, 'sex': True}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25b'), 'name': 'Charlotte_乙坂有宇', 'mobile': '123456', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25c'), 'name': 'Charlotte_友利奈绪', 'mobile': '654321', 'age': 16, 'sex': True}

# query = {"age":{"$lt":17}}        # age  <  17
# {'_id': ObjectId('5fd21cc92b280a7470998b7e'), 'name': 'nasa', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd21f0b722ca8317cddcc5c'), 'name': 'yeqi', 'sex': False, 'age': 15}
# {'_id': ObjectId('5fd21f267ae8ccfad62e7743'), 'name': 'yeqi', 'sex': False, 'age': 15}
# {'_id': ObjectId('5fd2206c81970531b2750b6b'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2230ff92b583773a1c8e3'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2231e58d8b8fe3b10c1d4'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25a'), 'name': '罪恶王冠_楪祈', 'mobile': '111111', 'age': 16, 'sex': True}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25c'), 'name': 'Charlotte_友利奈绪', 'mobile': '654321', 'age': 16, 'sex': True}

# query = {"age":{"$ne":17}}        # age  != 17
# {'_id': ObjectId('5fd21cc92b280a7470998b7e'), 'name': 'nasa', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd21f0b722ca8317cddcc5c'), 'name': 'yeqi', 'sex': False, 'age': 15}
# {'_id': ObjectId('5fd21f267ae8ccfad62e7743'), 'name': 'yeqi', 'sex': False, 'age': 15}
# {'_id': ObjectId('5fd2206c81970531b2750b6b'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2230ff92b583773a1c8e3'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2231e58d8b8fe3b10c1d4'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d258'), 'name': '罪恶王冠_恙神涯', 'mobile': '574158', 'age': 23, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25a'), 'name': '罪恶王冠_楪祈', 'mobile': '111111', 'age': 16, 'sex': True}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25c'), 'name': 'Charlotte_友利奈绪', 'mobile': '654321', 'age': 16, 'sex': True}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25d'), 'name': 'Charlotte_黑羽美砂', 'mobile': '999999', 'age': 18, 'sex': True}

# query = {"age":{"$in":[16,17]}}   # age in [16,17]
# {'_id': ObjectId('5fd21cc92b280a7470998b7e'), 'name': 'nasa', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2206c81970531b2750b6b'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2230ff92b583773a1c8e3'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2231e58d8b8fe3b10c1d4'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd22ca7a274c48b793f14b4'), 'name': '佐藤优一', 'mobile': '15025555666', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d259'), 'name': '罪恶王冠_樱满集', 'mobile': '777777', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25a'), 'name': '罪恶王冠_楪祈', 'mobile': '111111', 'age': 16, 'sex': True}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25b'), 'name': 'Charlotte_乙坂有宇', 'mobile': '123456', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25c'), 'name': 'Charlotte_友利奈绪', 'mobile': '654321', 'age': 16, 'sex': True}

# """
# query = {"age":{"$in":[17,18]}}
# {'_id': ObjectId('5fd22ca7a274c48b793f14b4'), 'name': '佐藤优一', 'mobile': '15025555666', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d259'), 'name': '罪恶王冠_樱满集', 'mobile': '777777', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25b'), 'name': 'Charlotte_乙坂有宇', 'mobile': '123456', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25d'), 'name': 'Charlotte_黑羽美砂', 'mobile': '999999', 'age': 18, 'sex': True}
# document_list = my_collections.find(query)
# for document in document_list:
#     print(document)

# 排序
"""
单个字段：
    sort("age",-1) # 倒序
    sort("age",1)  # 升序
多个字段：
    sort([("age",-1),("_id",1)])
"""

# document_list = my_collections.find().sort("age",-1)
# {'_id': ObjectId('5fd22d1969cd7dcfb865d258'), 'name': '罪恶王冠_恙神涯', 'mobile': '574158', 'age': 23, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25d'), 'name': 'Charlotte_黑羽美砂', 'mobile': '999999', 'age': 18, 'sex': True}
# {'_id': ObjectId('5fd22ca7a274c48b793f14b4'), 'name': '佐藤优一', 'mobile': '15025555666', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d259'), 'name': '罪恶王冠_樱满集', 'mobile': '777777', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25b'), 'name': 'Charlotte_乙坂有宇', 'mobile': '123456', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd21cc92b280a7470998b7e'), 'name': 'nasa', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2206c81970531b2750b6b'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2230ff92b583773a1c8e3'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2231e58d8b8fe3b10c1d4'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25a'), 'name': '罪恶王冠_楪祈', 'mobile': '111111', 'age': 16, 'sex': True}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25c'), 'name': 'Charlotte_友利奈绪', 'mobile': '654321', 'age': 16, 'sex': True}
# {'_id': ObjectId('5fd21f0b722ca8317cddcc5c'), 'name': 'yeqi', 'sex': False, 'age': 15}
# {'_id': ObjectId('5fd21f267ae8ccfad62e7743'), 'name': 'yeqi', 'sex': False, 'age': 15}

# document_list = my_collections.find().sort([("age",-1),("_id",1)])
# {'_id': ObjectId('5fd22d1969cd7dcfb865d258'), 'name': '罪恶王冠_恙神涯', 'mobile': '574158', 'age': 23, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25d'), 'name': 'Charlotte_黑羽美砂', 'mobile': '999999', 'age': 18, 'sex': True}
# {'_id': ObjectId('5fd22ca7a274c48b793f14b4'), 'name': '佐藤优一', 'mobile': '15025555666', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d259'), 'name': '罪恶王冠_樱满集', 'mobile': '777777', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25b'), 'name': 'Charlotte_乙坂有宇', 'mobile': '123456', 'age': 17, 'sex': False}
# {'_id': ObjectId('5fd21cc92b280a7470998b7e'), 'name': 'nasa', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2206c81970531b2750b6b'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2230ff92b583773a1c8e3'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd2231e58d8b8fe3b10c1d4'), 'name': '樱满集', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25a'), 'name': '罪恶王冠_楪祈', 'mobile': '111111', 'age': 16, 'sex': True}
# {'_id': ObjectId('5fd22d1969cd7dcfb865d25c'), 'name': 'Charlotte_友利奈绪', 'mobile': '654321', 'age': 16, 'sex': True}
# {'_id': ObjectId('5fd21f0b722ca8317cddcc5c'), 'name': 'yeqi', 'sex': False, 'age': 15}
# {'_id': ObjectId('5fd21f267ae8ccfad62e7743'), 'name': 'yeqi', 'sex': False, 'age': 15}
# for document in document_list:
#     print(document)



"""限制结果"""
# document_list = my_collections.find().limit(3)      # 只查询3条
# for document in document_list:
#     print(document)
# {'_id': ObjectId('5fd21cc92b280a7470998b7e'), 'name': 'nasa', 'sex': True, 'age': 16}
# {'_id': ObjectId('5fd21f0b722ca8317cddcc5c'), 'name': 'yeqi', 'sex': False, 'age': 15}
# {'_id': ObjectId('5fd21f267ae8ccfad62e7743'), 'name': 'yeqi', 'sex': False, 'age': 15}


"""删除文档"""
# 删除一个文档
# query = {"name":"樱满集"}
# ret = my_collections.delete_one(query)
# print(ret.deleted_count) # 1:删除成功 0:没有删除的数据


# 删除多个文档
# query = {"_id":"xiaoming1号"}
# ret = my_collection.delete_many(query)
# print(ret.deleted_count) # 大于0:删除成功 0:没有删除的数据

# 查询一条数据出来并删除
# 返回一条数据，如果没有，则返回None
# query = {"name":"xiaobai"}
# document = my_collection.find_one_and_delete(query)
# print(document)


"""更新文档"""
"""按条件更新一个文档的指定数据"""
# query = { "name": "xiaofei" }
# upsert = { "$set": { "age": 22 } }
# ret = my_collections.update_one(query, upsert)
# print(ret.modified_count) # 0 表示没有任何修改，1表示修改成功
#
# """按条件累加/累减指定数值一个文档的指定数据"""
# query = { "name": "xiaofei" }
# upsert = { "$inc": { "age": -1 } } # 累减
# # upsert = { "$inc": { "age": 1 } }  # 累加
# ret = my_collections.update_one(query, upsert)
# print(ret.modified_count)
#
# """更新多条数据"""
# # 把所有以"1"开头的手机码号的文档，全部改成999999
query = { "mobile": {"$regex":"^1"} }
upsert = { "$set": { "mobile": "999999" } }
ret = my_collections.update_many(query, upsert)
print(ret.modified_count)
