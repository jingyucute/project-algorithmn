'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-19 10:46:43
'''

# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

# 你的算法时间复杂度必须是 O(log n) 级别。

# 如果数组中不存在目标值，返回 [-1, -1]。

# 示例 1:

# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:

# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def searchRange(self, nums, target: int):

        def findIndex(nums, target, isLeft):
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target or (isLeft and nums[mid] == target):
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        leftIndex = findIndex(nums, target, True)

        if leftIndex >= len(nums) or nums[leftIndex] != target:
            # 连左边都找不到， 肯定没有这个数
            return [-1, -1]
        return [leftIndex, findIndex(nums, target, False) - 1]


if __name__ == '__main__':

    nums = [5, 7, 7, 8, 9, 10]
    target = 8
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.searchRange(nums, target)
    print(result)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
