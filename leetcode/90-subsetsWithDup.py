'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-25 00:21:47
'''

# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:

# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def subsetsWithDup(self, nums):
        result = []
        length = len(nums)
        nums.sort()

        def backTrack(index=0, path=[]):

            for i in range(index, length):
                path.append(nums[i])
                if path not in result:
                    result.append(path[:])
                    backTrack(i+1, path)
                path.pop()

        backTrack()
        result.append([])

        return result


if __name__ == '__main__':

    nums = [1, 2, 2]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.subsetsWithDup(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
