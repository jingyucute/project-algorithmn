'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-23 13:45:11
'''

# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:

# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def subsets(self, nums):
        result = [
        ]
        length = len(nums)

        def backTrack(index=0, path=[]):
            for i in range(index, length):
                path.append(nums[i])
                result.append(path.copy())
                backTrack(i + 1, path)
                path.pop()
        backTrack()
        result.append([])
        return result

    # 官方 , 递归
    def subsets1(self, nums):
        result = [
            []
        ]

        for num in nums:
            result += [cur + [num] for cur in result]
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.subsets1(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
