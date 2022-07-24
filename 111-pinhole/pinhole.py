"""
# 网络端口的转发和重定向

## 任务

将某个网络端口转发到另一个主机（forwarding），但可能会是不同的端口（redirecting）

## 解决方案

两个使用threading和socket模块的类就能完成我们需要的端口转发和重定向。

ref: https://cloud.tencent.com/developer/article/1569496
"""

import sys
import socket
import time
import threading

LOGGING = True
loglock = threading.Lock()


def log(s, *a):
    """打印日志到标准输出"""
    if LOGGING:
        loglock.acquire()
        try:
            print('%s:%s' % (time.ctime(), (s % a)))
            sys.stdout.flush()
        finally:
            loglock.release()


class PipeThread(threading.Thread):
    pipes = []  # 静态成员变量，存储通讯的线程编号
    pipeslock = threading.Lock()

    def __init__(self, source, sink):
        super(PipeThread, self).__init__()
        self.source = source
        self.sink = sink
        log('Creating new pipe thread %s (%s -> %s)', self, source.getpeername(), sink.getpeername())

        self.pipeslock.acquire()
        try:
            self.pipes.append(self)
        finally:
            self.pipeslock.release()

        self.pipeslock.acquire()
        try:
            pipes_now = len(self.pipes)
        finally:
            self.pipeslock.release()

        log('%s pipes now active', pipes_now)

    def run(self):
        while True:
            try:
                # 透传
                data = self.source.recv(1024)
                if not data:
                    break
                self.sink.send(data)
            except:
                break

        log('%s terminating', self)

        self.pipeslock.acquire()
        try:
            self.pipes.remove(self)
        finally:
            self.pipeslock.release()

        self.pipeslock.acquire()
        try:
            pipes_left = len(self.pipes)
        finally:
            self.pipeslock.release()

        log('%s pipes still active', pipes_left)


class Pinhole(threading.Thread):

    def __init__(self, port, newhost, newport):
        """
        :param port: 旧端口
        :param newhost: 新主机
        :param newport: 新端口
        """
        super(Pinhole, self).__init__()
        log('Redirecting: localhost: %s->%s:%s', port, newhost, newport)
        self.newhost = newhost
        self.newport = newport
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))
        self.sock.listen(5)     # 参数为timeout，单位为秒

    def run(self):
        while True:
            newsock, address = self.sock.accept()
            log('Creating new session for %s:%s', *address)
            fwd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            fwd.connect((self.newhost, self.newport))
            PipeThread(newsock, fwd).start()    # 正向传送
            PipeThread(fwd, newsock).start()    # 逆向传送


if __name__ == '__main__':
    print('Starting Pinhole port fowarder/redirector')

    try:
        port = int(sys.argv[1])
        newhost = sys.argv[2]
        try:
            newport = int(sys.argv[3])
        except IndexError:
            newport = port
    except (ValueError, IndexError):
        print('Usage: %s port newhost [newport]' % sys.argv[0])
        sys.exit(1)

    # sys.stdout = open('pinhole.log', 'w')      #将日志写入文件
    Pinhole(port, newhost, newport).start()
