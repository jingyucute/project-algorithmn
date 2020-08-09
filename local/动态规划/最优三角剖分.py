'''
Description: 
Author: jingyu
Date: 2020-08-08 13:26:48
LastEditors: Please set LastEditors
LastEditTime: 2020-08-09 09:14:09
'''


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime
g = [
    [0, 2, 3, 1, 5, 6],
    [2, 0, 3, 4, 8, 6],
    [3, 3, 0, 10, 13, 7],
    [1, 14, 10, 0, 12, 5],
    [5, 8, 13, 12, 0, 3],
    [6, 6, 7, 5, 3, 0],
]


def convexPolygonTriangulation():
    length = len(g[0])
    m = [[0 for j in range(length)] for i in range(length)]
    s = [[0 for j in range(length)] for i in range(length)]
    print(m)
    for d in range(2, length):
        for i in range(1, length-d+1):
            j = i + d - 1
            # Vi-1 Vi Vj
            m[i][j] = m[i+1][j] + g[i-1][i] + g[i][j] + g[i-1][j]
            s[i][j] = i
            for k in range(i+1, j):
                # Vi-1 Vi Vk Vj
                temp = m[i][k] + m[k+1][j] + g[i-1][k] + g[k][j] + g[i-1][j]
                if temp < m[i][j]:
                    m[i][j] = temp
                    s[i][j] = k
    print(m, m[1][5])
    print(s)


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    convexPolygonTriangulation()
    end_time = datetime.datetime.now()
    print(end_time-start_time)
