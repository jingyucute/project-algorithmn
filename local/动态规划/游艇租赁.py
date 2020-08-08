'''
Description: 
Author: jingyu
Date: 2020-08-08 13:26:48
LastEditors: Please set LastEditors
LastEditTime: 2020-08-08 17:08:24
'''


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime

c = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 6, 9, 15, 20],
    [0, 0, 0, 3, 5, 11, 18],
    [0, 0, 0, 0, 3, 6, 12],
    [0, 0, 0, 0, 0, 5, 8],
    [0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0]
]

# 第i行表示第几个港口, 如 c[1][2] 表示 1 -> 2 的租金


def rent():
    station = len(c[0]) - 1
    m = c
    s = [[0 for j in range(station + 1)] for i in range(station + 1)]

    # 当租出口大于2时， 才会出现选择方案 前 n- d 部分 和 后 d部分
    # for d in range(3, station + 1):
    #     for i in range(1, station - d + 2):
    #         j = i + d - 1
    #         for k in range(i+1, j):
    #             if m[i][j] > m[i][k] + m[k][j]:
    #                 m[i][j] = m[i][k] + m[k][j]
    #                 s[i][j] = k
    # print(m, m[1][6])

    for i in range(1, station):
        for j in range(i + 1, station + 1):
            if j - i > 1:
                for k in range(i+1, j):
                    if m[i][j] > m[i][k] + m[k][j]:
                        m[i][j] = m[i][k] + m[k][j]
                        if s[i][k]:
                            s[i][j] = s[i][k]
                        else:
                            s[i][j] = k
    print(m, m[1][6])
    printPath(s, 1, 6)


def printPath(s, i, j):
    if s[i][j] == 0:
        print("--", j)
        return
    printPath(s, i, s[i][j])
    printPath(s, s[i][j], j)


if __name__ == '__main__':

    start_time = datetime.datetime.now()

    rent()

    end_time = datetime.datetime.now()
    print(end_time-start_time)
