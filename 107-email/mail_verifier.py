"""
@Time    : 2022年05月03日
@Author  : 阏男秀
@File    : mail_verifier.py
"""
from smtplib import SMTP

user = input('请输入163邮箱：')
password = input('请输入授权码：')
email = input('请输入要验证的邮箱：')

with SMTP('smtp.163.com') as smtp:
    # smtp.set_debuglevel(1)

    # 登录邮箱
    smtp.login(user, password)

    # 使用MAIL FROM命令，向邮件服务器提供邮件的来源邮箱
    # 如果不设置直接调用rcpt命令，会返回 retcode (503); Msg: b'bad sequence of commands' 错误
    smtp.mail(user)

    # 使用RCPT TO命令，验证邮件地址是否存在
    res = smtp.rcpt(email)

    # (250, b'Mail OK') - 邮箱存在
    # (550, b'User not found: xxx@xxx.com') - 邮箱不存在
    print(res)
