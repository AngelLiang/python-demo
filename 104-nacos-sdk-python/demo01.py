import os
import nacos

# Both HTTP/HTTPS protocols are supported, if not set protocol prefix default is HTTP, and HTTPS with no ssl check(verify=False)
# "192.168.3.4:8848" or "https://192.168.3.4:443" or "http://192.168.3.4:8848,192.168.3.5:8848" or "https://192.168.3.4:443,https://192.168.3.5:443"
SERVER_ADDRESSES = os.getenv('NACOS_SERVER_ADDRESSES')
NAMESPACE = os.getenv('NACOS_NAMESPACE', None)

# no auth mode
client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE)
# auth mode
#client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, username="nacos", password="nacos")

# get config
data_id = "config.nacos"
group = "group"
print(client.get_config(data_id, group))

client.re
# 查询实例列表
print(client.list_naming_instance('test'))
