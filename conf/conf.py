#!/usr/bin/env python
# coding:utf-8
__author__ = 'Stone'
__date__ = '2018/05/30'

DEBUG = True

LOG_LEVEL = 'INFO'

# redis
base = {
    'seperator': ':',
    'maxkeylen': 100
}
socket_timeout = 2
scan_batch = 10000  # scan 限制获取数据量
show_key_self_count = False

mail_host = 'smtp.exmail.qq.com'
mail_user = 'test@test.com'
mail_pass = ''
mail_receivers = ["test@test.com", "test2@test.com"]
admin_mail = ["test@test.com"]  # 管理员邮箱

database = {
    "name": "redis_admin",
    "host": "192.168.11.209",
    "username": "uin",
    "password": "dba@123456",
    "port": "3306",
}
