# -*- coding: utf-8 -*-
__author__ = 'xujianbo'
import shutil
import threading
import zipfile
import os
import urllib
import re


"""
    下载最新浏览器driver
"""

"""
下载文件,解压并删除压缩包
"""


def down(url, name, file_path=None):
    if file_path == None:
        file_path = os.path.join(os.getcwd(), name + '.zip')
    if not os.path.exists(file_path):
        try:
            urllib.urlretrieve(url, file_path)
            # 解压文件并删除压缩包
            file_zip = zipfile.ZipFile(file_path, 'r')
            for file in file_zip.namelist():
                file_zip.extract(file, r'.')
            file_zip.close()
            os.remove(file_path)
        except:
            print '\nError when retrieving the URL:', file_path


"""
解压zip文件
"""


def decompression(file=None):
    # 解压文件
    if file == None:
        file_list = os.listdir(r'.')
    else:
        file_list = os.listdir(file)
    for file_name in file_list:
        if os.path.splitext(file_name)[1] == '.zip':

            file_zip = zipfile.ZipFile(file_name, 'r')
            for file in file_zip.namelist():
                file_zip.extract(file, r'.')
            file_zip.close()
            os.remove(file_name)


def update(str):
    # for str in drivername:
    if str == r'IEDriverServer':
        gcdriver_url = "http://npm.taobao.org/mirrors/selenium/IE.Driver.Beta/"
        response = urllib.urlopen(gcdriver_url).read()
        version_list = re.findall(
            r'Beta/IEDriverServer_beta_Win32_(.*?)\.zip">IEDriverServer_beta_Win32_(.*?)\.zip</a>',
            response)
    elif str != r'geckodriver':
        gcdriver_url = "http://npm.taobao.org/mirrors/" + str
        response = urllib.urlopen(gcdriver_url).read()
        version_list = re.findall(r'<a href="/mirrors/' + str + r'/(.*?)/">(.*?)/</a>', response)
    else:
        gcdriver_url = "http://npm.taobao.org/mirrors/" + str
        response = urllib.urlopen(gcdriver_url).read()
        version_list = re.findall(r'<a href="/mirrors/' + str + r'/v(.*?)/">v(.*?)/</a>', response)
    version_num = 0
    version = ''
    # 获取最新版本号
    for ver in range(0, len(version_list) - 1):
        num = int(version_list[ver][0].replace('.', ''))
        if num > version_num:
            version_num = num
            version = version_list[ver][0]
    # 获取最新版本下载地址
    if str == r'chromedriver':
        gcdown_url = "http://npm.taobao.org/mirrors/" + str + "/" + version + "/" + str + "_win32.zip"
    elif str == r'operadriver':
        gcdown_url = "http://npm.taobao.org/mirrors/" + str + "/" + version + "/" + str + "_win64.zip"
    elif str == r'IEDriverServer':
        gcdown_url = "http://npm.taobao.org/mirrors/selenium/IE.Driver.Beta/IEDriverServer_beta_Win32_" + version + ".zip"
    else:
        gcdown_url = "http://npm.taobao.org/mirrors/" + str + "/v" + version + "/" + str + "-v" + version + "-win64.zip"
    print "最新的" + str + "版本为：" + version + " 下载地址为：" + gcdown_url
    # 下载最新driver
    down(gcdown_url, str + '_' + version)
    # decompression()


def move():
    # 将operadriver.exe移动到browerDriver目录
    file = os.path.join(os.getcwd(), "operadriver_win64\\operadriver.exe")
    oper_file = os.path.join(os.getcwd(), "operadriver.exe")
    if os.path.exists(oper_file):
        os.remove(oper_file)
    shutil.move(file, os.path.join(os.getcwd()))
    # 删除文件夹operadriver_win64
    shutil.rmtree(os.path.join(os.getcwd(), "operadriver_win64"))


drivername = [r'geckodriver', r'chromedriver', r'operadriver', r'IEDriverServer']
threads = []


def main():
    n = range(len(drivername))
    for i in n:
        t = threading.Thread(target=update, args=(drivername[i],))
        threads.append(t)

    for i in n:
        threads[i].start()

    for i in n:
        threads[i].join()


if __name__ == '__main__':
    main()
    move()