'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 08:46:09
'''

# 峰值元素是指其值大于左右相邻值的元素。

# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

# 你可以假设 nums[-1] = nums[n] = -∞。

# 示例 1:

# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2:

# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 线性 O(n)
    def findPeakElement(self, nums) -> int:
        length = len(nums)
        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                return i
        return length - 1

    # 二分法
    def findPeakElement1(self, nums) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                # 峰值可能出现在左边
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':

    nums = [1, 2, 3, 1]

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.findPeakElement1(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
