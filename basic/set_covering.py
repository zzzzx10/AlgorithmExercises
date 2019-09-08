# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:16:16 2019

贪婪算法，集合覆盖问题
选出最少的广播台，能覆盖全部的州
"""

# 传入一个数组，转换为集合,表示需要被覆盖的州
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

#可供选择的广播台清单
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

#一个集合来存储最终选择的广播台
final_stations = set()

while states_needed:
    best_station = None    # 覆盖了最多的未覆盖州的广播台
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states  # 计算交集
        # 如果当前覆盖的范围更大，更新范围和station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered # 差集
    final_stations.add(best_station)

print(final_stations)