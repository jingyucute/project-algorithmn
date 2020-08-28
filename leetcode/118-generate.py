'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 12:53:32
'''

# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:

# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def generate(self, numRows: int):
        result = []

        for row in range(numRows):
            temp = []
            for col in range(row + 1):
                if col == 0 or col == row:
                    temp.append(1)
                else:
                    cur = result[row - 1][col - 1] + result[row-1][col]
                    temp.append(cur)
            result.append(temp[:])

        return result


if __name__ == '__main__':

    numRows = 5

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.generate(numRows)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
