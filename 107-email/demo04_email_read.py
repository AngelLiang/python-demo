import os
import poplib
from email.header import decode_header
from email.parser import Parser
from email.utils import parseaddr

email = os.getenv('MAIL_USER')
password = os.getenv('MAIL_PASS')
pop3_server = os.getenv('MAIL_POP')


def decode_str(s):
    """
    解析消息头中的字符串
    没有这个函数，print出来的会使乱码的头部信息。如'=?gb18030?B?yrXWpL3hufsueGxz?='这种
    通过decode，将其变为中文
    """
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    """
    获取邮件的字符编码
    首先在message中寻找编码，如果没有，就在header的Content-Type中寻找
    """
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos+8:].strip()
    return charset


def get_header(msg):
    """
    #解码邮件信息分为两个步骤，第一个是取出头部信息
    #首先取头部信息
    #主要取出['From','To','Subject']
    '''
    From: "=?gb18030?B?anVzdHpjYw==?=" <justonezcc@sina.com>
    To: "=?gb18030?B?ztLX1Ly6tcTTys/k?=" <392361639@qq.com>
    Subject: =?gb18030?B?dGV4dMTjusM=?=
    '''
    #如上述样式，均需要解码
    """

    for header in ['From', 'To', 'Subject']:
        value = msg.get(header, '')
        if value:
            # 文章的标题有专门的处理方法
            if header == 'Subject':
                value = decode_str(value)
            elif header in ['From', 'To']:
                # 地址也有专门的处理方法
                hdr, addr = parseaddr(value)
                name = decode_str(addr)
                #value = name + ' < ' + addr + ' > '
                value = name
        print(header + ':' + value)


def get_file(msg):
    for part in msg.walk():
        filename = part.get_filename()
        if filename is None:
            continue
        filename = decode_str(filename)  # 获取的文件是乱码名称，通过一开始定义的函数解码
        data = part.get_payload(decode=True)  # 取出文件正文内容
        # 此处可以自己定义文件保存位置
        path = filename
        with open(path, 'wb') as f:
            f.write(data)
            f.close()
            print(f'download:{filename}')


def get_content(msg):
    for part in msg.walk():
        content_type = part.get_content_type()
        charset = guess_charset(part)
        # 如果有附件，则直接跳过
        if part.get_filename() != None:
            continue
        email_content_type = ''
        content = ''
        if content_type == 'text/plain':
            email_content_type = 'text'
        elif content_type == 'text/html':
            print('html 格式 跳过')
            continue  # 不要html格式的邮件
            email_content_type = 'html'

        if charset:
            try:
                content = part.get_payload(decode=True).decode(charset)
            except AttributeError:
                print('type error')
            except LookupError:
                print("unknown encoding: utf-8")
        if email_content_type == '':
            continue
            # 如果内容为空，也跳过
        print(email_content_type + ' -----  ' + content)


def read_email():
    server = poplib.POP3(pop3_server)
    # server.set_debuglevel(1)
    server.user(email)
    server.pass_(password)
    print((pop3_server, email, password))

    print(server.stat())

    # list()返回所有邮件的编号:
    # resp, mails, octets = server.list()
    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]

    resp, mails, octets = server.top(1, 0)
    print(mails)

    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    # print(index)
    if index > 0:
        for i in range(1, index):
            print(i)
            resp, lines, octets = server.retr(i)  # 取邮件
            msg_content = b'\r\n'.join(lines).decode('utf-8', 'ignore')
            msg = Parser().parsestr(msg_content)
            get_header(msg)
            get_file(msg)
            get_content(msg)
            # server.dele(index)  # 删除邮件
    else:
        print('没有邮件')
    server.quit()


if __name__ == '__main__':
    read_email()
