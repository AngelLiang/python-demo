import os
import smtplib
from email.mime.text import MIMEText
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

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("发送测试", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
