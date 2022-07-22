import os
import json
import pprint

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.vpc.v20170312 import vpc_client, models

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, override=True)

SECRETID = os.getenv('SecretId')
SECRETKEY = os.getenv('SecretKey')
REGION = os.getenv('region')
SECURITYGROUPID = os.getenv('SecurityGroupId')
Port = '10082'

if not SECRETID or not SECRETKEY:
    raise ValueError('SecretId is null or SecretKey is null')


# class Response(models.ModifySecurityGroupPoliciesResponse):
#     pass


class TencentSecurityGroup:
    def __init__(self, SecretId, SecretKey, region, SecurityGroupId) -> None:
        self.SecretId = SecretId
        self.SecretKey = SecretKey
        self.region = region
        self.SecurityGroupId = SecurityGroupId

        # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
        # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
        self.cred = credential.Credential(self.SecretId, self.SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "vpc.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        self.client = vpc_client.VpcClient(self.cred, region, clientProfile)

    def gen_params(self, port, action='ACCEPT'):
        """
        action: str, "ACCEPT" OR "DROP"
        """
        # 实例化一个请求对象,每个接口都会对应一个request对象
        params = {
            "SecurityGroupId": self.SecurityGroupId,
            "SecurityGroupPolicySet": {
                # 入站规则
                "Ingress": [
                    {
                        "Protocol": "TCP",
                        "Port": str(port),
                        "Action": action,
                    }
                ]
            }
        }
        return params

    def gen_req(self, params) -> models.ModifySecurityGroupPoliciesResponse:
        req = models.ModifySecurityGroupPoliciesRequest()
        req.from_json_string(json.dumps(params))
        # 返回的resp是一个ModifySecurityGroupPoliciesResponse的实例，与请求对象对应
        self.resp = self.client.ModifySecurityGroupPolicies(req)
        return self.resp

    def get_resp_json(self):
        return json.loads(self.resp.to_json_string())

    def modify_port(self, port):
        params = self.gen_params(port)
        self.gen_req(params)
        return self.resp


try:
    tsg = TencentSecurityGroup(SECRETID, SECRETKEY, REGION, SECURITYGROUPID)
    resp = tsg.modify_port(20058)
    print(resp)
except TencentCloudSDKException as err:
    print(err)
