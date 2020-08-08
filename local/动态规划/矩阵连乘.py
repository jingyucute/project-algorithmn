'''
Description: 
Author: jingyu
Date: 2020-08-08 13:26:48
LastEditors: Please set LastEditors
LastEditTime: 2020-08-08 18:14:23
'''


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime
matrix = [3, 5, 10, 8, 2, 4]
# 5个矩阵 3*5 5*10 10*8 8*2 2*4


def matrixChain():
    nums = len(matrix) - 1  # 矩阵个数
    m = [[0 for j in range(nums + 1)] for i in range(nums + 1)]
    s = [[0 for j in range(nums + 1)] for i in range(nums + 1)]
    # 扩大连乘矩阵个数, 也就是m按照\对角线来填表
    for r in range(2, nums+1):
        for i in range(1, nums - r + 2):  # i <= nums -r + 1 ==> nums - i + 1 >= r
            j = i + r - 1  # j - i + 1 = r 保证是r个矩阵相乘
            # 默认 矩阵相乘是后面的先乘， 再和第一个相乘
            m[i][j] = m[i+1][j] + matrix[i-1]*matrix[i]*matrix[j]
            s[i][j] = i
            for k in range(i+1, j):
                temp = m[i][k] + m[k+1][j] + matrix[i-1]*matrix[k]*matrix[j]
                if temp < m[i][j]:
                    m[i][j] = temp
                    s[i][j] = k

    print(m, m[1][5])
    print(s)


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    matrixChain()
    end_time = datetime.datetime.now()
    print(end_time-start_time)
