import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host = os.getenv('MAIL_HOST')
mail_user = os.getenv('MAIL_USER')
mail_pass = os.getenv('MAIL_PASS')

sender = os.getenv('MAIL_SENDER')

# 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = os.getenv('MAIL_RECEIVERS')
if ',' in receivers:
    receivers = receivers.split(',')


# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("来自于", 'utf-8')
message['To'] = Header("发送于", 'utf-8')
subject = 'Python SMTP 邮件测试1234'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('邮件正文', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
