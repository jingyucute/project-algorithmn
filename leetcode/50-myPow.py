'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 17:34:10
'''


# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。

# 示例 1:

# 输入: 2.00000, 10
# 输出: 1024.00000
# 示例 2:

# 输入: 2.10000, 3
# 输出: 9.26100
# 示例 3:

# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
# 说明:

# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1]


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 分治法
        def quickMul(x, N):
            if N == 0:
                return 1.0
            y = quickMul(x, N // 2)
            if N % 2 == 0:
                return y * y
            else:
                return y * y * x

        if n >= 0:
            return quickMul(x, n)
        else:
            return 1.0 / quickMul(x, -n)


if __name__ == '__main__':
    x = 2.10000
    n = 3
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.myPow(x, n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
