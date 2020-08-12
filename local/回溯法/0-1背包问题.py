'''
Description: 
Author: jingyu
Date: 2020-08-12 10:32:31
LastEditors: Please set LastEditors
LastEditTime: 2020-08-12 16:45:14
'''
#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime
import random


def Bound(index, N, v, data_list):
    rv = 0
    while index <= N:
        rv += v[index]
        index += 1
    return data_list[1] + rv


def Backtrack(index, N, W, w, v, data_list):

    if index > N:
        data_list[2] = data_list[1]
        for i in range(1, N+1):
            data_list[6][i] = data_list[5][i]
        return
    if data_list[0] + w[index] <= W:
        # 前面选择的总重量 + 当前物品的重量 没有超重， 放入, 递归求解
        data_list[5][index] = 1
        data_list[0] += w[index]
        data_list[1] += v[index]
        Backtrack(index+1, N, W, w, v, data_list)
        # 回溯到当前结点
        data_list[0] -= w[index]
        data_list[1] -= v[index]

    # 如果加入剩余的节点的价值大于 当前的价值， 决定 是否递归
    # 在这里进行判断， 可以减小搜索空间， 提高效率，
    # 在叶子节点进行最优判断也可以操作
    if Bound(index + 1, N, v, data_list) > data_list[2]:
        data_list[5][index] = 0
        Backtrack(index+1, N, W, w, v, data_list)


def Knapsack(N, W, w, v):
    cw = 0
    cv = 0
    bestv = 0
    sumv = 0
    sumw = 0
    x = [0]
    bestx = [0]
    for i in range(1, N + 1):
        sumw += w[i]
        sumv += v[i]
        x.append(0)
        bestx.append(0)

    if sumw <= W:
        bestv = sumv
        print("最大价值:", bestv)
        return

    data_list = [
        cw, cv, bestv, sumw, sumv, x, bestx
    ]
    # data_list 是为了传递引用， 好恶心的操作
    Backtrack(1, N, W, w, v, data_list)
    print("最大价值:", data_list[2])
    print("放入物品序列号:")
    for i in range(1, N+1):
        if data_list[6][i] == 1:
            print(i)


if __name__ == '__main__':
    # N = int(input("请输入物品个数:"))
    # W = int(input("请输入容器容量:"))
    # w = [0]
    # v = [0]
    # x = [0]
    # bestx = [0]
    # for i in range(1, N+1):
    #     # w.append(int(input()))
    #     # v.append(int(input()))
    #     w.append(random.randint(1, W // 2 + 1))
    #     v.append(random.randint(1, 20))
    #     x.append(0)
    #     bestx.append(0)

    N = 5
    W = 10
    w = [0, 2, 5, 4, 2, 3]
    v = [0, 6, 3, 5, 4, 6]

    print(w)
    print(v)
    start_time = datetime.datetime.now()
    Knapsack(N, W, w, v)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
