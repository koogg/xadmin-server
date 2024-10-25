#!/usr/bin/env python
# -*- coding:utf-8 -*-
# project : xadmin-server
# filename : setting
# author : ly_13
# date : 10/18/2024

from .base import *

# 密码安全配置
SECURITY_PASSWORD_MIN_LENGTH = 8
SECURITY_ADMIN_USER_PASSWORD_MIN_LENGTH = 8
SECURITY_PASSWORD_UPPER_CASE = True
SECURITY_PASSWORD_LOWER_CASE = True
SECURITY_PASSWORD_NUMBER = True
SECURITY_PASSWORD_SPECIAL_CHAR = False
SECURITY_PASSWORD_RULES = [
    'SECURITY_PASSWORD_MIN_LENGTH',
    'SECURITY_PASSWORD_UPPER_CASE',
    'SECURITY_PASSWORD_LOWER_CASE',
    'SECURITY_PASSWORD_NUMBER',
    'SECURITY_PASSWORD_SPECIAL_CHAR'
]

# 用户登录限制的规则
SECURITY_LOGIN_LIMIT_COUNT = 7
SECURITY_LOGIN_LIMIT_TIME = 30  # Unit: minute
SECURITY_CHECK_DIFFERENT_CITY_LOGIN = True
# 登录IP限制的规则
SECURITY_LOGIN_IP_BLACK_LIST = []
SECURITY_LOGIN_IP_WHITE_LIST = []
SECURITY_LOGIN_IP_LIMIT_COUNT = 50
SECURITY_LOGIN_IP_LIMIT_TIME = 30

# 登陆规则
SECURITY_LOGIN_ACCESS_ENABLED = True
SECURITY_LOGIN_CAPTCHA_ENABLED = True
SECURITY_LOGIN_ENCRYPTED_ENABLED = True
SECURITY_LOGIN_TEMP_TOKEN_ENABLED = True
SECURITY_LOGIN_BY_EMAIL_ENABLED = True
SECURITY_LOGIN_BY_SMS_ENABLED = False
SECURITY_LOGIN_BY_BASIC_ENABLED = True

# 注册规则
SECURITY_REGISTER_ACCESS_ENABLED = True
SECURITY_REGISTER_CAPTCHA_ENABLED = True
SECURITY_REGISTER_ENCRYPTED_ENABLED = True
SECURITY_REGISTER_TEMP_TOKEN_ENABLED = True
SECURITY_REGISTER_BY_EMAIL_ENABLED = True
SECURITY_REGISTER_BY_SMS_ENABLED = False
SECURITY_REGISTER_BY_BASIC_ENABLED = True
# 忘记密码规则
SECURITY_RESET_PASSWORD_ACCESS_ENABLED = True
SECURITY_RESET_PASSWORD_CAPTCHA_ENABLED = True
SECURITY_RESET_PASSWORD_TEMP_TOKEN_ENABLED = True
SECURITY_RESET_PASSWORD_ENCRYPTED_ENABLED = True
SECURITY_RESET_PASSWORD_BY_EMAIL_ENABLED = True
SECURITY_RESET_PASSWORD_BY_SMS_ENABLED = False

# 绑定邮箱
SECURITY_BIND_EMAIL_ACCESS_ENABLED = True
SECURITY_BIND_EMAIL_CAPTCHA_ENABLED = True
SECURITY_BIND_EMAIL_TEMP_TOKEN_ENABLED = True
SECURITY_BIND_EMAIL_ENCRYPTED_ENABLED = True

# 绑定手机
SECURITY_BIND_PHONE_ACCESS_ENABLED = True
SECURITY_BIND_PHONE_CAPTCHA_ENABLED = True
SECURITY_BIND_PHONE_TEMP_TOKEN_ENABLED = True
SECURITY_BIND_PHONE_ENCRYPTED_ENABLED = True

# 基本配置
SITE_URL = 'http://127.0.0.1:8000'
FRONT_END_WEB_WATERMARK_ENABLED = True  # 前端水印展示
PERMISSION_FIELD_ENABLED = True  # 字段权限控制
PERMISSION_DATA_ENABLED = True  # 数据权限控制
REFERER_CHECK_ENABLED = False  # referer 校验

# 验证码配置
VERIFY_CODE_TTL = 5 * 60  # Unit: second
VERIFY_CODE_LIMIT = 60
VERIFY_CODE_LENGTH = 6
VERIFY_CODE_LOWER_CASE = False
VERIFY_CODE_UPPER_CASE = False
VERIFY_CODE_DIGIT_CASE = True

# 邮件配置
EMAIL_ENABLED = False
EMAIL_HOST = ""
EMAIL_PORT = 465
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_FROM = ""
EMAIL_RECIPIENT = ""
EMAIL_SUBJECT_PREFIX = "Xadmin-Server "
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

# 短信配置
SMS_ENABLED = False
SMS_BACKEND = 'alibaba'
SMS_TEST_PHONE = ''

# 阿里云短信配置
ALIBABA_ACCESS_KEY_ID = ''
ALIBABA_ACCESS_KEY_SECRET = ''
ALIBABA_VERIFY_SIGN_NAME = ''
ALIBABA_VERIFY_TEMPLATE_CODE = ''

# 图片验证码
CAPTCHA_IMAGE_SIZE = (120, 40)  # 设置 captcha 图片大小
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_LENGTH = 4  # 字符个数,仅针对随机字符串生效
CAPTCHA_TIMEOUT = 5  # 超时(minutes)
CAPTCHA_FONT_SIZE = 22
CAPTCHA_BACKGROUND_COLOR = "#ffffff"
CAPTCHA_FOREGROUND_COLOR = "#001100"
CAPTCHA_NOISE_FUNCTIONS = ("captcha.helpers.noise_arcs", "captcha.helpers.noise_dots")

# 下面图片验证码 默认配置
CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
# CAPTCHA_NOISE_FUNCTIONS = ("captcha.helpers.noise_arcs", "captcha.helpers.noise_dots")
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_FONT_PATH = os.path.join(BASE_DIR, "captcha", "fonts", "Vera.ttf")
CAPTCHA_LETTER_ROTATION = (-35, 35)
CAPTCHA_FILTER_FUNCTIONS = ("captcha.helpers.post_smooth",)
CAPTCHA_PUNCTUATION = """_"',.;:-"""
CAPTCHA_FLITE_PATH = None
CAPTCHA_SOX_PATH = None
CAPTCHA_MATH_CHALLENGE_OPERATOR = "*"
CAPTCHA_GET_FROM_POOL = False
CAPTCHA_GET_FROM_POOL_TIMEOUT = 5
CAPTCHA_2X_IMAGE = True