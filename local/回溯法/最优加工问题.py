'''
Description:
Author: jingyu
Date: 2020-08-12 22:58:31
LastEditors: Please set LastEditors
LastEditTime: 2020-08-13 15:28:31
'''
#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime
import random


def BackTack(index, N, list, data_list):
    if index > N:
        if data_list[1] < data_list[2]:
            data_list[4] = []
        a = []
        for n in data_list[3]:
            a.append(n)
        data_list[4].append(a)
        data_list[2] = data_list[1]
    else:
        for i in range(index, N+1):
            data_list[0] += list[data_list[3][i]][0]
            temp = data_list[1]
            data_list[1] = max(data_list[1], data_list[0]) + \
                list[data_list[3][i]][1]
            if data_list[1] < data_list[2]:
                t_temp = data_list[3][index]
                data_list[3][index] = data_list[3][i]
                data_list[3][i] = t_temp
                BackTack(index+1, N, list, data_list)
                t_temp = data_list[3][index]
                data_list[3][index] = data_list[3][i]
                data_list[3][i] = t_temp
            data_list[0] -= list[data_list[3][i]][0]
            data_list[1] = temp


if __name__ == '__main__':

    # N = int(input("输入机器零件的个数:"))
    # list = [[0, 0]]
    # for i in range(1, N + 1):
    #     x, y = int(input()), int(input())
    #     list.append([x, y])

    N = 6
    list = [[0, 0], [5, 7], [1, 2], [8, 2], [5, 4], [3, 7], [4, 4]]
    print(list)
    result = []

    f1, f2 = 0, 0  # 在机器1、2上所用的时间
    bestf = 50000
    x = [i for i in range(N + 1)]  # 存放当前第几个零件
    result = []
    data_list = [
        f1, f2,  bestf, x, result
    ]

    start_time = datetime.datetime.now()
    BackTack(1, N, list, data_list)
    print("最优加工时间:", data_list[2])
    print("加工顺序(从下标1开始)", data_list[4])
    end_time = datetime.datetime.now()
    print(end_time-start_time)
