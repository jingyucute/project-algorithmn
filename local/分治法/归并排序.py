'''
Description: 
Author: jingyu
Date: 2020-08-07 13:13:41
LastEditors: Please set LastEditors
LastEditTime: 2020-08-07 15:27:28
'''
#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime
import random


def merge(list, low, mid, high):
    i = low
    j = mid+1
    new_list = []
    while i <= mid and j <= high:
        if (list[i] < list[j]):
            new_list.append(list[i])
            i = i + 1
        else:
            new_list.append(list[j])
            j = j + 1
    while i <= mid:
        new_list.append(list[i])
        i = i + 1
    while j <= high:
        new_list.append(list[j])
        j = j + 1
    for i in range(len(new_list)):
        list[low+i] = new_list[i]
        i = i + 1


def mergeSort(list, low, high):

    if low < high:
        mid = (low + high) // 2
        mergeSort(list, low, mid)
        mergeSort(list, mid+1, high)
        merge(list, low, mid, high)


if __name__ == '__main__':
    # start_time = datetime.datetime.now()
    # end_time = datetime.datetime.now()
    # print(end_time-start_time)
    n = int(input("请输入数列中的元素个数n为:"))

    list = []
    for i in range(n):
        list.append(random.randint(1, 5000000))
    print("排序前:", list)
    # print("请依次输入数据")
    # list = [int(input()) for i in range(n)]

    # list = [42, 15, 20, 6, 8, 38, 50, 12]
    start_time = datetime.datetime.now()
    mergeSort(list, 0, n-1)
    end_time = datetime.datetime.now()
    print("排序后:", list)
    print("排序时间", end_time-start_time)

    # 记录一下, 100w 数据排序时间 0:00:07.511946
