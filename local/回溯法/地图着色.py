#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime
import random


def check(index, map, data):
    for j in range(1, index):
        if map[j][index] == 1 and data[1][j] == data[1][index]:
            return False
    return True


def BackTack(index, N, M,  map, data):
    if index > N:
        # 到达叶子节点
        data[0] += 1
        a = []
        for i in range(len(data[1])):
            a.append(data[1][i])

        data[2].append(a)
    else:
        # 第 i 个节点上色
        for color in range(1, M+1):
            data[1][index] = color  # 这里修改的东西， 会影响最引用的结果
            if check(index, map, data):
                BackTack(index+1, N, M, map, data)


if __name__ == '__main__':

    # N = int(input("输入节点数:"))
    # M = int(input("输入颜色数:"))
    # print("输入无向图的邻接矩阵:")
    # E = int(input("请输入边数:"))
    # print("请输入有边相连的两个节点")
    # map = [[0 for j in range(N + 1)] for i in range(N + 1)]
    # for i in range(E):
    #     u, v = int(input()), int(input())
    #     map[u][v], map[v][u] = 1, 1

    N = 7
    M = 3
    E = 12
    map = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 1, 0]
    ]
    sum = 0  # 方案总数
    t = [0 for i in range(N + 1)]  # 当前节点对应染色
    result = []
    data = [
        sum, t,  result
    ]
    start_time = datetime.datetime.now()
    BackTack(1, N, M, map, data)
    print(data)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
