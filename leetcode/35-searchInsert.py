'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-19 11:32:31
'''

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 你可以假设数组中无重复元素。

# 示例 1:

# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:

# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:

# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:

# 输入: [1,3,5,6], 0
# 输出: 0


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # 这里就是没有找到的
        nums.insert(low, target)
        return low


if __name__ == '__main__':

    nums = []
    target = 0
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.searchInsert(nums, target)
    print(result, nums)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
