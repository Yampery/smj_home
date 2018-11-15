#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @author: Yampery
# @date: 2018/11/14 23:19

from django.db import models


# 微信用户个人信息
class UserInfo:
    openid = models.CharField(max_length=64, db_index=True)
    subscribe = models.IntegerField(max_length=1, default=2)
    subscribeTime = models.CharField(max_length=32, null=True)
    nickname = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=32, null=True)
    sex = models.IntegerField(max_length=1, default=2)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    province = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=255, null=True)
    headimgurl = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=11, null=True)

    class Meta:
        db_table = 'wx_user'


# 商品表
class Product:
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    class Meta:
        db_table = 'smj_product'


# 商品品牌
class Brand:
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    letter = models.CharField(max_length=1)

    class Meta:
        db_table = 'smj_brand'


# 商品