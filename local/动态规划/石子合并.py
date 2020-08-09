'''
Description: 
Author: jingyu
Date: 2020-08-08 13:26:48
LastEditors: Please set LastEditors
LastEditTime: 2020-08-09 11:21:44
'''


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime
import random
a = [0]


def straight():
    length = len(a) - 1
    sum = []  # 前 i 堆石子总数
    temp = 0
    for i in range(length + 1):
        temp += a[i]
        sum.append(temp)
    min = [[0 for j in range(length + 1)] for i in range(length + 1)]
    max = [[0 for j in range(length + 1)] for i in range(length + 1)]

    for d in range(2, length + 1):
        for i in range(1, length - d + 2):
            j = i + d - 1
            # print('--', i, '--', j, '--')
            temp = sum[j] - sum[i-1]   # i -> j 堆的石子总数

            min[i][j] = min[i+1][j] + temp
            max[i][j] = max[i+1][j] + temp
            for k in range(i+1, j):
                if min[i][j] > min[i][k] + min[k+1][j] + temp:
                    min[i][j] = min[i][k] + min[k+1][j] + temp
                if max[i][j] < max[i][k] + max[k+1][j] + temp:
                    max[i][j] = max[i][k] + max[k+1][j] + temp
    print(min[1][length])
    print(max[1][length])


if __name__ == '__main__':

    n = int(input("请输入有多少堆石子:"))
    for i in range(1, n + 1):
        a.append(random.randint(1, 3000))
    print(a)
    start_time = datetime.datetime.now()
    straight()
    end_time = datetime.datetime.now()
    print(end_time-start_time)

    #  时间复杂度 O(n^3)
    #  规模输入1000堆时， 运行时间 0:01:32.355134 有点长哈
    #  100  -->  0:00:00.081880
