'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 19:55:53
'''

# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

# 示例 1:

# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:

# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        status = [
            [False] * n for _ in range(m)
        ]
        result = []
        # direct = 1(右), 2(下) , 3(左), 4(上)
        direct = 1
        row, col = 0, 0
        for _ in range(m * n):
            status[row][col] = True
            result.append(matrix[row][col])
            # print(row, col, matrix[row][col], status[row][col])

            if direct == 1:
                if col + 1 == n or status[row][col+1] == True:
                    direct = 2
                    row += 1
                else:
                    col += 1
            elif direct == 2:
                if row + 1 == m or status[row+1][col] == True:
                    direct = 3
                    col -= 1
                else:
                    row += 1
            elif direct == 3:
                if col - 1 < 0 or status[row][col - 1] == True:
                    direct = 4
                    row -= 1
                else:
                    col -= 1
            else:
                if row - 1 < 0 or status[row - 1][col] == True:
                    direct = 1
                    col += 1
                else:
                    row -= 1

        return result

    # 官方答案， 思路一样， 但是这个更简洁
    # 这个思路的区别在于， 这个相当于给了一个边框，按照边框来遍历
    # 遍历完一层后， 边框就向内收缩一层
    def spiralOrder1(self, matrix):
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.spiralOrder1(matrix)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
