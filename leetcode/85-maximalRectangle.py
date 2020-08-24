'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-24 16:59:19
'''

# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

# 示例:

# 输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 没思路， 看的官方解答
    def maximalRectangle(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        R, C = len(matrix), len(matrix[0])
        dp = [[0] * C for _ in range(R)]
        maxArea = 0
        for row in range(R):
            for col in range(C):
                if matrix[row][col] == '0':
                    continue
                if col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row][col-1] + 1
                width = dp[row][col]
                for k in range(row, -1, -1):
                    width = min(width, dp[k][col])
                    maxArea = max(maxArea, width * (row - k + 1))

        return maxArea


if __name__ == '__main__':
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.maximalRectangle(matrix)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
