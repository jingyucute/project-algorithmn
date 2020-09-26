'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 17:26:20
'''
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

# 示例 1:

# 输入: 1
# 输出: true
# 解释: 20 = 1
# 示例 2:

# 输入: 16
# 输出: true
# 解释: 24 = 16
# 示例 3:

# 输入: 218
# 输出: false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/power-of-two
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n = n // 2
        return n == 1


if __name__ == '__main__':
    n = 4
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.isPowerOfTwo(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
