from application import json_rpc
import re,random,json
# from status import APIStatus as status
# from message import ErrorMessage as message
# from ronglian_sms_sdk import SmsSDK
from flask import current_app
from application import redis
from .models import Book_text,Book
from application.settings.dev import Config
from flask import render_template

def index():
    # return ren
    data = {
        'img': 'lingzhou.jpg',
        'name': '灵舟',
        'text': '道家修炼今生，佛家修炼来世！ 道在此岸，佛在彼岸，人在中间！ 灵舟不在此岸，不在彼岸，不在中间！ ………… 这是一个浩瀚的奇异世界，有与天搏命的修行者，婀娜多姿的美妙女子，穿越寰宇的古强人，还有凶猛的古兽，黑石中的白骨，泥土下的黄泉，天空中的宫殿。 还有七只古老的灵舟…… ……',
        'author': '九当家',
        'state': '完结',
        'num': '15183947',
        'type': '玄幻'
    }
    return render_template("pages/index.html", **data)
def detail(user_id):
    print(user_id)
    data = {
        'user_id': user_id,
        'img': 'lingzhou.jpg',
        'name': '灵舟',
        'text': '道家修炼今生，佛家修炼来世！ 道在此岸，佛在彼岸，人在中间！ 灵舟不在此岸，不在彼岸，不在中间！ ………… 这是一个浩瀚的奇异世界，有与天搏命的修行者，婀娜多姿的美妙女子，穿越寰宇的古强人，还有凶猛的古兽，黑石中的白骨，泥土下的黄泉，天空中的宫殿。 还有七只古老的灵舟…… ……',
        'author': '九当家',
        'state': '完结',
        'num': '15183947',
        'type': '玄幻',
        'qwq': '''    道家修炼今生，佛家修炼来世！
    道在此岸，佛在彼岸，人在中间！
    灵舟不在此岸，不在彼岸，不在中间！
    …………
    这是一个浩瀚的奇异世界，有与天搏命的修行者，婀娜多姿的美妙女子，穿越寰宇的古强人，还有凶猛的古兽，黑石中的白骨，泥土下的黄泉，天空中的宫殿。
    还有七只古老的灵舟……
    ……
    《灵舟》1群：213252123（主群）　《灵舟》2群：123410001　《灵舟》3群：123290199
    《灵舟》vip群：230435654（17k的vip读者可加，进群发截图。）
    各位书友要是觉得《灵舟》还不错的话请不要忘记向您QQ群和微博里的朋友推荐哦！
''',
        "content": ''
  }
    return render_template('pages/detail.html', **data)


def read(user_id):
    book_data = Book_text.query.get(user_id)
    data = {
        'book_name': book_data.book_chapter,
        'chapter_text': eval(book_data.chapter_text)
    }

    return render_template('pages/turn.html', **data)

# @json_rpc.method(name="Home.sms")
# def sms(mobile):
#     """发送短信验证码"""
#     # 验证手机
#     if not re.match("^1[3-9]\d{9}$",mobile):
#         return {"errno": status.CODE_VALIDATE_ERROR, "errmsg": message.mobile_format_error}
#
#     # 短信发送冷却时间
#     ret = redis.get("int_%s" % mobile)
#     if ret is not None:
#         return {"errno": status.CODE_INTERVAL_TIME, "errmsg": message.sms_interval_time}
#
#     # 生成验证码
#     print('qwq生成验证码........................................')
#     sms_code = "%06d" % random.randint(0,999999)
#     print(sms_code)
#     try:
#         print('7777777777777777777777777')
#         # 异步发送短信
#         from mycelery.sms.tasks import send_sms
#         # from mycelery.sms.tasks import send_sms
#         print('7777777777777777777777777')
#         send_sms.delay(mobile=mobile, sms_code=sms_code)
#         print(        send_sms.delay(mobile=mobile, sms_code=sms_code))
#         # 返回结果
#         return {"errno":status.CODE_OK, "errmsg": message.sms_is_send}
#     except Exception as e:
#         return {"errno": status.CODE_SMS_ERROR, "errmsg": message.sms_send_error}
#
#
#
#
#
#




















# @json_rpc.method(name="Home.sms")
# def sms(mobile):
#     """发送短信验证码"""
#     # 验证手机
#     if not re.match("^1[3-9]\d{9}$",mobile):
#         return {"errno": status.CODE_VALIDATE_ERROR, "errmsg": message.mobile_format_error}
#
#     # 短信发送冷却时间
#     ret = redis.get("int_%s" % mobile)
#     if ret is not None:
#         return {"errno": status.CODE_INTERVAL_TIME, "errmsg": message.sms_interval_time}
#
#     # 容联云接口:
#     from ronglian_sms_sdk import SmsSDK
#
#     accId = Config.SMS_ACCOUNT_ID
#     accToken = Config.SMS_ACCOUNT_TOKEN
#     appId = Config.SMS_APP_ID
#
#     # def send_message():
#     #     sdk = SmsSDK(accId, accToken, appId)
#     #     tid = '1'
#     #     mobile = '15025555653'
#     #     datas = (1,3)
#     #     resp = sdk.sendMessage(tid, mobile, datas)
#     #     print('-------------------------------------------',resp)
#     #
#     # send_message()
#
#
#
#
#
#
#     # 生成验证码
#     sms_code = "%06d" % random.randint(0,999999)
#     # 发送短信
#     sdk = SmsSDK(
#         current_app.config.get("SMS_ACCOUNT_ID"),
#         current_app.config.get("SMS_ACCOUNT_TOKEN"),
#         current_app.config.get("SMS_APP_ID")
#     )
#     ret = sdk.sendMessage(
#         current_app.config.get("SMS_TEMPLATE_ID"),
#         mobile,
#         (sms_code, current_app.config.get("SMS_EXPIRE_TIME") // 60)
#     )
#     print(ret)
#     result = json.loads(ret)
#     if result["statusCode"] == "000000":
#         pipe = redis.pipeline()
#         pipe.multi()  # 开启事务
#         # 保存短信记录到redis中
#         pipe.setex("sms_%s" % mobile,current_app.config.get("SMS_EXPIRE_TIME"),sms_code)
#         # 进行冷却倒计时
#         pipe.setex("int_%s" % mobile,current_app.config.get("SMS_INTERVAL_TIME"),"_")
#         pipe.execute() # 提交事务
#         # 返回结果
#         return {"errno":status.CODE_OK, "errmsg": message.ok}
#     else:
#         # return {"errno":status.CODE_OK, "errmsg": message.ok}
#         return {"errno": status.CODE_SMS_ERROR, "errmsg": message.sms_send_error}


# def index(id):
#     # current_app.log.error('qwq错了！')
#     return 'indexQwQ去这是参数:{}'.format(id)




