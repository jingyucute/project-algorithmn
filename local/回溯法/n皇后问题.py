'''
Description: 
Author: jingyu
Date: 2020-08-12 22:58:31
LastEditors: Please set LastEditors
LastEditTime: 2020-08-12 23:17:11
'''
#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime
import random


def check(index, list):
    for i in range(1, index):
        if list[i] == list[index] or index - i == abs(list[index]-list[i]):
            return False
    return True


def BackTack(index, N, list, result):
    if index > N:
        # 到达叶子节点
        a = []
        for place in list:
            a.append(place)
        result.append(a)
    else:
        # 第i个皇后
        for i in range(1, N + 1):
            list[index] = i
            # 判断该位置是否合适
            if check(index, list):
                BackTack(index+1, N, list, result)


if __name__ == '__main__':

    N = int(input("输入皇后的个数:"))
    list = [0] * (N + 1)
    result = []
    start_time = datetime.datetime.now()
    BackTack(1, N, list, result)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
