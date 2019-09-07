# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 16:45:42 2019

迪杰斯特拉算法
需要三个哈希表：
    图的结构graph
    当前到个节点的最短路径值costs
    当前节点的最优父节点parents

每个边的权重，用的是hash里面的hash graph["start"]["end"]
cost["node"]表示起点到该点的cost
parents["node"] 同上
"""

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# costs table, 从起点到各点的cost
infinity = float("inf") # 表示正无穷
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

#记录处理过的节点
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 在未处理的节点中找出开销最小的节点
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node] # 遍历当前节点的所有邻居
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # 如果新的开销更小，更新cost,换父节点
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node 
    processed.append(node)  # Mark the node as processed.
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)
