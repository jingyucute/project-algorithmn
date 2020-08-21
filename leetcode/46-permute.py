'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 14:15:19
'''

# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。

# 示例:

# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def permute(self, nums):
        n = len(nums)

        result = []
        if n == 0:
            return result

        def backTrack(first=0):
            if first == n:
                result.append(nums.copy())
            else:
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    backTrack(first+1)
                    nums[first], nums[i] = nums[i], nums[first]

        backTrack()

        return result


if __name__ == '__main__':
    nums = []
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.permute(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
