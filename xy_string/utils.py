# -*- coding: UTF-8 -*-
__author__ = 'helios'
__doc__ = 'utils'
'''
  * @File    :   utils.py
  * @Time    :   2023/06/04 13:36:02
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
'''

from xy_type.utils import empty_value


def is_empty_string(a_string) -> bool:
    return not isinstance(a_string, str) or len(a_string) <= 0 or not a_string


def empty_string(a_string, default) -> str | None:
    if is_empty_string(a_string=a_string) and is_empty_string(default):
        return None
    return empty_value(a_string, str, default)


import re


def contains_zh(a_string) -> bool:
    if is_empty_string(a_string):
        return False
    zh_pattern = re.compile("[\u4e00-\u9fa5]+")
    match = zh_pattern.search(str(a_string))
    if match:
        return True
    return False
