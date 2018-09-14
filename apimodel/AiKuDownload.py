# -*- coding: utf-8 -*-
"""
__author__: 'xujianbo'
__date__:  '2018/9/13'
爬取爱酷网站(http://www.icoolxue.com)上所有课程视频
@:param url 课程首页地址，如：http://www.icoolxue.com/album/show/140
"""
import threading
from api.ProgressBar import ProgressBar
import os
from api.HttpRequest import SendHttpRequest
from api import apipub


def download(url, path=None):
    response = SendHttpRequest().urlOpen(url)
    list = apipub.findall(r'<a href="(.*?)" class="play-holder-Video', response)
    title_list = apipub.findall('<span class=title>(.*?)</span>', response)
    directory_name = apipub.findall('<div class=album-title>\\n<h1>(.*?)</h1>', response)[0].encode("gbk")
    thread_list = []
    for ur in list:
        header = {
            "client": "web",
            "Referer": "http://www.icoolxue.com" + ur
        }
        title = title_list[list.index(ur)]
        if path == None:
            directory_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "video",
                directory_name)
        else:
            directory_path = os.path.join(path.encode("gbk"), directory_name)
        if os.path.exists(directory_path) == False:
            os.makedirs(directory_path)
        save_path = os.path.join(directory_path, title.encode("gbk") + ".mp4")
        download_url = \
            SendHttpRequest().get("http://www.icoolxue.com/video/play/url/" + ur.split("/")[-1], headers=header)["data"]
        t = threading.Thread(target=ProgressBar().download, args=(download_url, save_path, title,))
        thread_list.append(t)
        # t.setDaemon(True) # 设置为True时主线程结束后子线程会被迫结束
        t.start()
    for th in thread_list:
        th.join()
    print "\n课程：" + directory_name.encode("utf-8") + "下载完成"