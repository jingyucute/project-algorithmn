'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 12:21:34
'''

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？


# 网格中的障碍物和空位置分别用 1 和 0 来表示。

# 说明：m 和 n 的值均不超过 100。

# 示例 1:

# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        map = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    map[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        map[i][j] = 1
                    elif i == 0 and j != 0:
                        map[i][j] = map[i][j-1]
                    elif i != 0 and j == 0:
                        map[i][j] = map[i-1][j]
                    elif i != 0 and j != 0:
                        map[i][j] = map[i-1][j] + map[i][j-1]
        # print(obstacleGrid)
        # print(map)
        return map[row-1][col-1]


if __name__ == '__main__':
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.uniquePathsWithObstacles(obstacleGrid)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
