# -*- coding: utf-8 -*-
__author__ = 'xujianbo'
__date__ = '2018/9/13'
"""
爬取爱酷网站(http://www.icoolxue.com)上所有课程视频
@:param url 课程首页地址，如：http://www.icoolxue.com/album/show/140
"""
import os
import requests
from api.HttpRequest import SendHttpRequest
from api import apipub


def download(url):
    response = SendHttpRequest().urlOpen(url)
    list = apipub.findall(r'<a href="(.*?)" class="play-holder-Video', response)
    title_list = apipub.findall('<span class=title>(.*?)</span>', response)
    directory_name = apipub.findall('<div class=album-title>\\n<h1>(.*?)</h1>', response)[0].encode("gbk")
    for ur in list:
        header = {
            "client": "web",
            "Referer": "http://www.icoolxue.com" + ur
        }
        title = title_list[list.index(ur)]
        directory_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "video",
            directory_name)
        if os.path.exists(directory_path) == False:
            os.mkdir(directory_path)
        path = os.path.join(directory_path, title.encode("gbk") + ".mp4")
        download_url = \
            SendHttpRequest().get("http://www.icoolxue.com/video/play/url/" + ur.split("/")[-1], headers=header)["data"]
        with open(path, 'wb') as fp:
            fp.write(requests.get(download_url).content)
        fp.close()
        print("当前视频：" + title + "下载完成！")