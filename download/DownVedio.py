# -*- coding: utf-8 -*-

__author__ = 'lovex'
__date__ = '2018/9/12'

from apimodel import AiKuDownload

# list = [216, 261, 267, 140, 317, 112, 316, 364, 365, 378, 369]
list = [201]
for nu in list:
    AiKuDownload.download('http://www.icoolxue.com/album/show/' + str(nu), path="F:\\教学视频")