'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-20 15:39:23
'''

# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。

#  

# 示例 1:

# 输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
# 示例 2:

# 输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        R, C = len(grid), len(grid[0])
        lands = 0

        def dfs(row, col):
            directs = [
                (1, 0), (-1, 0), (0, 1), (0, -1)
            ]
            grid[row][col] = '0'
            for direct in directs:
                x, y = row + direct[0], col + direct[1]
                if 0 <= x < R and 0 <= y < C and grid[x][y] == '1':
                    dfs(x, y)

        for row in range(R):
            for col in range(C):
                if grid[row][col] == '1':
                    lands += 1
                    dfs(row, col)
        return lands


if __name__ == '__main__':

    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.numIslands(grid)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
