#!/usr/loca/bin/python
# -*- coding: utf-8 -*-

class C:
    def __init__(self):
        print("我是__init__方法")
    def __del__(self):
        print("我是__del__发NGFA")
C1=C()
C2=C1
C3=C2

