'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-20 16:25:50
'''

# 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

# 示例 1: 

# 输入: [5,7]
# 输出: 4
# 示例 2:

# 输入: [0,1]
# 输出: 0

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        shift = 0
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift


if __name__ == '__main__':
    m, n = 5, 7
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.rangeBitwiseAnd(m, n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
