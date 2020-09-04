'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 17:08:56
'''

# 给定一个整数 n，返回 n! 结果尾数中零的数量。

# 示例 1:

# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
# 示例 2:

# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
# 说明: 你算法的时间复杂度应为 O(log n)

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            count += n // 5
            n = n // 5
        return count


if __name__ == '__main__':

    n = 20

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.trailingZeroes(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
