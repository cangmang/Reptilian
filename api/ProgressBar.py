# -*- coding: utf-8 -*-
__author__ = 'Administrator'
__date__ = '2018/9/13'
from contextlib import closing
import requests

"""
下载文件并显示下载进度
"""


class ProgressBar(object):
    def __init__(self):
        self.total = 100.0
        self.count = 0.0

    def __view_bar(self, count=1):
        self.count += count
        rate = self.count / self.total
        rate_num = int(rate * 100)
        number = int(50 * rate)
        r = '\r[%s%s]%d%%' % ("#" * number, " " * (50 - number), rate_num, )
        print "\r {}".format(r),  # \r回到行的开头

    """
    下载文件
    @:param url 下载地址
    @:param save_path 保存路径
    """

    def download(self, url, save_path):
        with closing(requests.get(url, stream=True)) as response:
            chunk_size = 40960  # 单次请求最大值
            self.total = int(response.headers['content-length'])  # 内容体总大小
            with open(save_path, "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    self.__view_bar(count=len(data))