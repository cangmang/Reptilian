# -*- coding: utf-8 -*-
import os
import urllib
from api.HttpRequest import SendHttpRequest

__author__ = 'lovex'
__date__ = '2018/9/12'

from apimodel import AiKuDownload

list = [364, 365, 378, 369]
# list = [261, 267, 140, 317, 112, 316, 216,201]
for nu in list:
    AiKuDownload.download('http://www.icoolxue.com/album/show/' + str(nu), path="F:\\教学视频")