'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-03 23:07:59
'''

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 请找出其中最小的元素。

# 你可以假设数组中不存在重复元素。

# 示例 1:

# 输入: [3,4,5,1,2]
# 输出: 1
# 示例 2:

# 输入: [4,5,6,7,0,1,2]
# 输出: 0

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 简单点 线性遍历吧
    def findMin(self, nums) -> int:
        # return min(nums)
        if not nums:
            return 0
        minNum = nums[0]
        for num in nums:
            if num < minNum:
                minNum = num
        return minNum

    # 二分
    def findMin1(self, nums) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]

        left, right = 0, length - 1
        if nums[right] > nums[left]:
            return nums[left]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                # 左边有序
                left = mid + 1
            else:
                right = mid - 1


if __name__ == '__main__':

    nums = [3, 4, 5, 1, 2]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.findMin1(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
