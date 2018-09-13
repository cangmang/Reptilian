# -*- coding: utf-8 -*-
import re

__author__ = 'lovex'
__date__ = '2018/9/12'


def findall(regular_expression, response):
    return re.findall(regular_expression, response)


def match(regular_expression, response):
    return re.match(regular_expression, response)
