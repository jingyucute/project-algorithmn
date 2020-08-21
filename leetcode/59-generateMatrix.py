'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 00:45:34
'''

# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

# 示例:

# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def generateMatrix(self, n: int):
        map = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        index = 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                map[top][column] = index
                index += 1
            for row in range(top+1, bottom+1):
                map[row][right] = index
                index += 1
            if left < right and top < bottom:
                for column in range(right - 1, left - 1, -1):
                    map[bottom][column] = index
                    index += 1
                for row in range(bottom - 1, top, -1):
                    map[row][left] = index
                    index += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        print(map)

        return map


if __name__ == '__main__':
    n = 3
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.generateMatrix(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
