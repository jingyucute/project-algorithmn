'''
Description: 
Author: jingyu
Date: 2020-08-08 13:26:48
LastEditors: Please set LastEditors
LastEditTime: 2020-08-08 13:49:01
'''


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


def editDistance(str1, str2):
    print(str1, str2)
    len1 = len(str1)
    len2 = len(str2)
    list = [[0 for j in range(len2+1)] for i in range(len1+1)]
    for i in range(len1 + 1):
        list[i][0] = i  # str1 和 空串的 编辑距离
    for j in range(len2+1):
        list[0][j] = j  # str2 和 空串的 编辑距离
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            diff = 0        # 判断 当前 str1[i-1] 和 str2[j-1] 是否相同
            if str1[i-1] != str2[j - 1]:
                diff = 1
            # 判断 Xn-1 和 Ym 的解 和 Xn 和 Ym-1 的解是否为 Xn 和 Ym的最优解
            temp = min(list[i-1][j], list[i][j-1]) + 1
            list[i][j] = min(temp, list[i-1][j-1] + diff)
    return list[len1][len2]


if __name__ == '__main__':
    str1 = "FAMILY"
    str2 = "FARME"

    start_time = datetime.datetime.now()
    print("最短编辑距离", editDistance(str1, str2))

    end_time = datetime.datetime.now()
    print(end_time-start_time)
