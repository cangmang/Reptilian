# -*- coding: utf-8 -*-
__author__ = 'xujianbo'
__data__ = '2018-03-20'
"""
"""
import logging
import datetime
import os

logLevel = {
    1: logging.NOTSET,
    2: logging.DEBUG,
    3: logging.INFO,
    4: logging.WARNING,
    5: logging.ERROR,
    6: logging.CRITICAL
}
root_dir = os.path.dirname(__file__)
loggers = {}
# 定义日志方法,从配置文件读取日志等级,且定义日志输出路径
def log(**kwargs):
    global loggers
    log_level = 3
    log_path = os.path.join(os.path.dirname(root_dir) + "\\logs")
    if os.path.exists(log_path):
        log_file = os.path.join(log_path, datetime.datetime.now().strftime('%Y-%m-%d_%H_%M') + '.log')
    else:
        os.mkdir(r'%s' % log_path)
        log_file = os.path.join(log_path, datetime.datetime.now().strftime('%Y-%m-%d_%H_%M') + '.log')
    logger = logging.getLogger()

    logger.setLevel(log_level)
    if not logger.handlers:
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(log_file)
        fh.setLevel(log_level)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        loggers.update(dict(name=logger))
    return logger