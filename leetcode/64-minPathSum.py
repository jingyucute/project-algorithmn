'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 12:50:34
'''

# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。

# 示例:

# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def minPathSum(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif i != 0 and j != 0:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        print(dp)
        return dp[row-1][col-1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.minPathSum(grid)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
