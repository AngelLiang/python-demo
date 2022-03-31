# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models


import os
import json

from random_code import generate_random_code

ACCESS_KEY_ID = os.getenv('ALIYUN_ACCESS_KEY_ID')
ACCESS_KEY_SECRET = os.getenv('ALIYUN_ACCESS_KEY_SECRET')
TEST_PHONE = os.getenv('ALIYUN_TEST_PHONE')
TEMPLATE_CODE = os.getenv('ALIYUN_TEMPLATE_CODE')
SIGN_NAME = os.getenv('ALIYUN_SIGN_NAME')
TEMPLATE_PARAM = json.dumps({"code": generate_random_code()})


class SendSMS:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Dysmsapi20170525Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'dysmsapi.aliyuncs.com'
        return Dysmsapi20170525Client(config)

    @staticmethod
    def send_message(template_param):
        client = SendSMS.create_client(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            sign_name=SIGN_NAME,
            phone_numbers=TEST_PHONE,
            template_code=TEMPLATE_CODE,
            template_param=template_param
        )
        # 复制代码运行请自行打印 API 的返回值
        client.send_sms(send_sms_request)

    @staticmethod
    def main(args: List[str]) -> None:
        client = SendSMS.create_client(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            sign_name=SIGN_NAME,
            phone_numbers=TEST_PHONE,
            template_code=TEMPLATE_CODE,
            template_param=TEMPLATE_PARAM
        )
        # 复制代码运行请自行打印 API 的返回值
        client.send_sms(send_sms_request)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = SendSMS.create_client(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            sign_name=SIGN_NAME,
            phone_numbers=TEST_PHONE,
            template_code=TEMPLATE_CODE,
            template_param=TEMPLATE_PARAM
        )
        # 复制代码运行请自行打印 API 的返回值
        await client.send_sms_async(send_sms_request)


if __name__ == '__main__':
    # SendSMS.main(sys.argv[1:])
    SendSMS.send_message(template_param=TEMPLATE_PARAM)
