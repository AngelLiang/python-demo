from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkdysmsapi.request.v20170525.SendSmsRequest import SendSmsRequest

import os

ACCESS_KEY_ID = os.getenv('ALIYUN_ACCESS_KEY_ID')
ACCESS_KEY_SECRET = os.getenv('ALIYUN_ACCESS_KEY_SECRET')
TEST_PHONE = os.getenv('ALIYUN_TEST_PHONE')
ALIYUN_TEMPLATE_CODE = os.getenv('ALIYUN_TEMPLATE_CODE')

credentials = AccessKeyCredential(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
# use STS Token
# credentials = StsTokenCredential('<your-access-key-id>', '<your-access-key-secret>', '<your-sts-token>')
client = AcsClient(region_id='cn-qingdao', credential=credentials)

request = SendSmsRequest()
request.set_accept_format('json')

request.set_PhoneNumbers(TEST_PHONE)  # 接收短信的手机号码
request.set_SignName("阿里云")  # 短信签名名称
request.set_TemplateCode(ALIYUN_TEMPLATE_CODE)  # 短信模板CODE

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
