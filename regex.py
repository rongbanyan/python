# coding:utf-8
# 强口令
"""
写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。强口令的定义是：长度不少于8 个字符，同时包含大写和小写字符，至少有一位数字。你可能需要用多个正则表达式来测试该字符串，以保证它的强度。
"""

import re

def checkPassword(password):
    passwordReg = re.compile(r'''
        (?=^.{8,}$)         # 八位数以上
        (?![.\n])           # 不能有换行符
        (?=(.*\d+))         # 至少有一个数字
        (?=.*[a-z])         # 包含大写字母
        (?=.*[A-Z])         # 包含小写字母
        ''', re.VERBOSE)
    result = passwordReg.match(password)
    if result:
        return True
    else:
        return False

print (checkPassword('12geaesA'))