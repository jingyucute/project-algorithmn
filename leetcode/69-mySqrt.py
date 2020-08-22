'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 18:06:57
'''


# 实现 int sqrt(int x) 函数。

# 计算并返回 x 的平方根，其中 x 是非负整数。

# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

# 示例 1:

# 输入: 4
# 输出: 2
# 示例 2:

# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return 0
        if x == 0 or x == 1:
            return x

        for i in range(x // 2 + 2):
            q = i * i
            if q < x:
                continue
            elif q == x:
                return i
            else:
                return i - 1

    def mySqrt1(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    x = 2
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.mySqrt(x)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
