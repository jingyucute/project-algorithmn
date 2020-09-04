'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 19:47:17
'''

# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

# 示例 1:

# 输入: [10,2]
# 输出: 210
# 示例 2:

# 输入: [3,30,34,5,9]
# 输出: 9534330
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':

    nums = [
        3, 30, 34, 5, 9
    ]

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.largestNumber(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
