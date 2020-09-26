'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 11:44:43
'''

# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

# 示例:

# 输入:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# 输出: 4

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximal-square
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 暴力法 居然过了测试
    def maximalSquare(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        R, C = len(matrix), len(matrix[0])
        maxSide = 0
        for row in range(R):
            for col in range(C):
                if matrix[row][col] == '1':
                    maxSide = max(maxSide, 1)
                    curMaxSide = min(R - row, C - col)
                    for k in range(1, curMaxSide):
                        flag = True
                        if matrix[row + k][col + k] == '0':
                            break
                        for m in range(k):
                            if matrix[row + m][col + k] == '0' or matrix[row + k][col + m] == '0':
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k + 1)
                        else:
                            break

        return maxSide**2

    # dp
    def maximalSquare1(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        R, C = len(matrix), len(matrix[0])
        dp = [[0] * C for _ in range(R)]
        print(dp)
        maxSide = 0

        for row in range(R):
            for col in range(C):
                if matrix[row][col] == '1':
                    if row == 0 or col == 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = min(
                            dp[row - 1][col], dp[row][col - 1], dp[row-1][col-1]) + 1
                    maxSide = max(maxSide, dp[row][col])

        return maxSide**2


if __name__ == '__main__':
    matrix = [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0']
    ]
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.maximalSquare1(matrix)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
