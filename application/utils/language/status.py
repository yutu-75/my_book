class APIStatus():
    CODE_OK = 1000 # 接口操作成功
    CODE_VALIDATE_ERROR = 1001   # 验证有误！
    CODE_SMS_ERROR = 1002        # 短信功能执行失败
    CODE_INTERVAL_TIME = 1003    # 短信发送冷却中
    CODE_NO_AUTHORIZATION = 1004  # 请求中没有附带认证信息
    CODE_SIGNATURE_EXPIRED = 1005 # 请求中的认证信息已过期
    CODE_INVALID_AUTHORIZATION = 1006 # 请求中的认证信息无效
    CODE_NO_ACCOUNT = 1007 # 请求中没有账户信息
    CODE_NO_USER = 1008 # 用户不存在
    CODE_PASSWORD_ERROR = 1009 # 密码错误
    CODE_CAPTCHA_ERROR = 1010 # 验证码验证失败
    CODE_TRANSACTION_PASSWORD_ERROR = 1011 # 交易密码和确认密码不一致
    CODE_UPDATE_USER_RELATION_ERROR = 1012 # 更新用户好友申请状态失败
    CODE_RECHARGE_ERROR=1013 # 充值发生错误
    CODE_NO_MONEY = 1014  # 余额不足
    CODE_NO_PACKAGE = 1015  # 背包存储达到上限
    CODE_NO_CREDIT = 1016  # 果子不足
    CODE_NO_EMPTY = 1017  # 没有空余的栏位
    CODE_NO_SUCH_PET = 1018 # 没有该宠物
    CODE_NO_SUCH_PROP = 1018  # 没有该道具
    CODE_NO_PET = 1019 # 没有宠物
    CODE_NO_FEED = 1020 # 饱食度超过90%，不能喂养

    CODE_PASSWORD_FORMAT_ERROR = 10012 # 密码格式错误



