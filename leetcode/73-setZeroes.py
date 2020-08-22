'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 22:16:10
'''

# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

# 示例 1:

# 输入:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 示例 2:

# 输入:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# 进阶:

# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row, col = len(matrix), len(matrix[0])
        row_list = []
        col_list = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if i not in row_list:
                        row_list.append(i)
                    if j not in col_list:
                        col_list.append(j)
        for i in row_list:
            for j in range(col):
                matrix[i][j] = 0
        for j in col_list:
            for i in range(row):
                matrix[i][j] = 0

    # 官方 , 思路一样， 但是看着简洁多了
    def setZeroes1(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0


if __name__ == '__main__':
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    start_time = datetime.datetime.now()
    solution = Solution()
    solution.setZeroes1(matrix)
    print(matrix)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
