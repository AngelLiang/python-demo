import os
from time import sleep
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


res = client.add_naming_instance('test1', '192.168.31.250', 9000)
print(res)
res = client.add_naming_instance('test2', '192.168.31.251', 9000)
print(res)

# 查询实例列表
print(client.list_naming_instance('test'))


while True:
    res = client.send_heartbeat('test1', '192.168.31.250', 9000)
    print(res)
    sleep(5)
