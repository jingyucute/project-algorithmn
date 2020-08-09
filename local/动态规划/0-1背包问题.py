'''
Description:
Author: jingyu
Date: 2020-08-08 13:26:48
LastEditors: Please set LastEditors
LastEditTime: 2020-08-09 15:15:40
'''

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime
import random


def maxValueInPackage(N, W, w, v):
    # N 个数
    # W 容器容量
    # w w[i] 对应的是第i个物品的重量
    # v v[i] 对应的是第i个物品的价值
    list = [[0 for j in range(W + 1)] for i in range(N + 1)]
    # list[i][j] 表示的是前i个物品放入容量为j的容器的价值, list[N[W]就是我们要求的结果
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j < w[i]:
                # 不够放入第i个物品
                list[i][j] = list[i-1][j]
            else:
                # 可以决策放还是不放,根据其价值来
                if list[i-1][j] > list[i-1][j - w[i]] + v[i]:
                    #   不放 价值更大
                    list[i][j] = list[i-1][j]
                else:
                    # 放 价值更大
                    list[i][j] = list[i-1][j - w[i]] + v[i]
    print(list, list[N][W])


if __name__ == '__main__':

    N = int(input("请输入物品个数:"))
    W = int(input("请输入容器容量:"))
    w = [0]
    v = [0]
    for i in range(1, N+1):
        # w.append(int(input()))
        # v.append(int(input()))
        w.append(random.randint(1, W // 2 + 1))
        v.append(random.randint(1, 20))

    # w = [0, 2, 5, 4, 2, 3]
    # v = [0, 6, 3, 5, 4, 6]
    # N = 5
    # W = 10

    print(w)
    print(v)

    start_time = datetime.datetime.now()
    maxValueInPackage(N, W, w, v)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
