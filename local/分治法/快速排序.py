import datetime
import random


def partition(list, low, high):
    pivot = list[low]
    while low < high:
        while low < high and list[high] > pivot:
            high = high - 1
        list[low] = list[high]
        while low < high and list[low] <= pivot:
            low = low + 1
        list[high] = list[low]
    list[low] = pivot
    return low


def quickSort(list, low, high):
    if low < high:
        mid = partition(list, low, high)
        quickSort(list, low, mid-1)
        quickSort(list, mid+1, high)


if __name__ == '__main__':

    # list = [42, 15, 20, 6, 8, 38, 50, 12]

    n = int(input("请输入数列中的元素个数n为:"))

    list = []
    for i in range(n):
        list.append(random.randint(1, 5000000))
    print("排序前:", list)

    start_time = datetime.datetime.now()
    quickSort(list, 0, n-1)
    end_time = datetime.datetime.now()
    print("排序后:", list)
    print("排序时间", end_time-start_time)

    # 记录一下 100w数据 排序时间 0:00:03.826490
