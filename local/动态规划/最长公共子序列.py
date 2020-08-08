'''
Description:
Author: jingyu
Date: 2020-08-08 09:10:56
LastEditors: Please set LastEditors
LastEditTime: 2020-08-08 11:03:50
'''


# eg s1="ABCADAB"
#    s2="BACDBA"
# result s="BADB" len=4

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


def LCSL(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    list = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]
    path = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i - 1] == str2[j - 1]:
                list[i][j] = list[i-1][j-1] + 1
                path[i][j] = 1
            else:
                if list[i-1][j] > list[i][j-1]:
                    list[i][j] = list[i-1][j]
                    path[i][j] = 2   # 从上一行下来
                else:

                    list[i][j] = list[i][j-1]
                    path[i][j] = 3   # 从左侧过来

    common_len = list[len1][len2]
    path_list = []
    pathList(path, str1, len1, len2, path_list)
    print(common_len, path_list)


def pathList(path, str, i, j, result):
    if i == 0 or j == 0:
        return
    if path[i][j] == 1:
        pathList(path, str, i-1, j-1, result)
        result.append(str[i-1])
    else:
        if path[i][j] == 2:
            pathList(path, str, i-1, j, result)
        else:
            pathList(path, str, i, j-1, result)


if __name__ == '__main__':
    str1 = "ABCADAB"
    str2 = "BACDBA"
    start_time = datetime.datetime.now()
    LCSL(str1, str2)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
