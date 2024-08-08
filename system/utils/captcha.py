#!/usr/bin/env python
# -*- coding:utf-8 -*-
# project : server
# filename : captcha
# author : ly_13
# date : 6/6/2023
import logging

from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.conf import settings

logger = logging.getLogger(__name__)


class CaptchaAuth(object):
    def __init__(self, captcha_key=''):
        self.captcha_key = captcha_key

    def __get_captcha_obj(self):
        return CaptchaStore.objects.filter(hashkey=self.captcha_key).first()

    def generate(self):
        self.captcha_key = CaptchaStore.generate_key(settings.CAPTCHA_CHALLENGE_FUNCT)
        captcha_image = captcha_image_url(self.captcha_key)
        captcha_obj = self.__get_captcha_obj()
        code_length = 0
        if captcha_obj:
            code_length = len(captcha_obj.response)
        return {"captcha_image": captcha_image, "captcha_key": self.captcha_key, "length": code_length}

    def valid(self, verify_code):
        captcha_obj = self.__get_captcha_obj()
        logger.info(f"captcha_key:{self.captcha_key} verify_code:{verify_code}  challenge:{captcha_obj}")
        if captcha_obj:
            if self.captcha_key and verify_code and verify_code.strip(" ").lower() == captcha_obj.response.lower():
                return True
        return False
