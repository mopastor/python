#!/usr/bin/env python
# -*- coding: utf-8 -*-

class GrandPa:
    def __init__(self):
        print ('I\'m GrandPa')
        
class Father(GrandPa):
    def __init__(self):
        print ('I\'m Father')
        
class son(Father):
    """A simple example class"""
    i = 12345
    def __init__(self):
        print ('这是构造函数，son')
    def sayHello(self):
        return 'hello world'
        
if __name__ == '__main__':
    son = son()
    #类型帮主信息
    print ('类型帮主信息：', son.__doc__)
    #类型名称：
    print ('类型名称：', son.__name__)
    #类型所继承的基类
    print ('类型所继承的基类', son.__bases__)
    #类型字典
    print ('类型字典：', son.__dict__)
    #类型呢所在模块
    print ('类型所在模块：', son.__module__)
    #类型实例
    print ('类型实例：', son.__class__)