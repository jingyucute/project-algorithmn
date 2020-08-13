'''
Description: 
Author: jingyu
Date: 2020-08-12 22:58:31
LastEditors: Please set LastEditors
LastEditTime: 2020-08-13 18:07:47
'''
#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime
import random


def traveling(index, N, list, data_list):
    if index > N:
        if list[data_list[2][N]][data_list[2][1]] != 50000:
            if data_list[0] + list[data_list[2][N]][data_list[2][1]] > data_list[1]:
                return

            if data_list[0] + list[data_list[2][N]][data_list[2][1]] < data_list[1]:
                data_list[3] = []

            a = []
            for l in data_list[2]:
                a.append(l)
            data_list[3].append(a)
            data_list[1] = data_list[0] + \
                list[data_list[2][N]][data_list[2][1]]
    else:
        for j in range(index, N + 1):
            if list[data_list[2][index-1]][data_list[2][j]] != 50000 and data_list[0] + list[data_list[2][index-1]][data_list[2][j]] < data_list[1]:
                # 如果当前的节点和上一个节点相连， 而且走过的距离加上这两个节点间的距离还比较小

                temp = data_list[2][index]
                data_list[2][index] = data_list[2][j]
                data_list[2][j] = temp
                data_list[0] += list[data_list[2]
                                     [index - 1]][data_list[2][index]]
                traveling(index+1, N, list, data_list)
                data_list[0] -= list[data_list[2]
                                     [index - 1]][data_list[2][index]]
                temp = data_list[2][index]
                data_list[2][index] = data_list[2][j]
                data_list[2][j] = temp


if __name__ == '__main__':

    # N = int(input("输入景点个数:"))
    # E = int(input("景点之间的连线数(边数):"))
    # # 定义50000为很大的数， 不可及
    # list = [[50000 for j in range(N + 1)] for j in range(N + 1)]

    # for i in range(1, E + 1):
    #     u, v, w = int(input()), int(input()), int(input())
    #     list[u][v], list[v][u] = w, w

    N = 5
    E = 9
    list = [
        [50000, 50000, 50000, 50000, 50000, 50000],
        [50000, 50000, 3, 50000, 8, 9],
        [50000, 3, 50000, 3, 10, 5],
        [50000, 50000, 3, 50000, 4, 3],
        [50000, 8, 10, 4, 50000, 20],
        [50000, 9, 5, 3, 20, 50000]
    ]
    cl = 0
    bestl = 50000
    x = [i for i in range(N + 1)]
    result = []
    data_list = [
        cl, bestl, x, result
    ]
    start_time = datetime.datetime.now()
    #   从第2个节点开始, 默认从第一个节点出发
    traveling(2, N, list, data_list)
    print("最短路径长度为:", data_list[1])
    print("共有%s种方案:" % (len(data_list[3])))
    print(data_list[3])
    end_time = datetime.datetime.now()
    print(end_time-start_time)
