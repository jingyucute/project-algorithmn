'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-20 17:30:50
'''

# 统计所有小于非负整数 n 的质数的数量。

# 示例:

# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def countPrimes(self, n: int) -> int:
        import math
        flag = [True] * n
        for i in range(2, math.ceil(math.sqrt(n))):
            if flag[i]:
                for j in range(i**2, n, i):
                    flag[j] = False

        count = 0
        for i in range(2, n):
            if flag[i]:
                count += 1
        return count


if __name__ == '__main__':

    n = 10
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.countPrimes(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
