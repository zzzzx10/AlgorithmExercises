# -*- coding: utf-8 -*-
"""
用字典来存储哈希表
字典有两种定义方式
"""

phone_book = dict()
phone_book["jenny"] = 8675309
phone_book["emergency"] = 911
print (phone_book["jenny"])


voted = {} 

def check_voter(name):
  if voted.get(name): # 元素在散列表中，函数get将返回对应值；否则返回None
    print("kick them out!")
  else:
    voted[name] = True
    print("let them vote!")

check_voter("tom")
check_voter("mike")
check_voter("mike")
