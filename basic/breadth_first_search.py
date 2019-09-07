# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:11:15 2019

广度优先搜索
利用的是队列deque() 弹出左边元素是popleft,增加元素直接+=
"""
from collections import deque
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # 记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person+" is a mango seller!")
                #searched.append(person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def person_is_seller(name):
    return name[-1] == 'm'


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search("you")