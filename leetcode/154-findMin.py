'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 00:10:01
'''

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 请找出其中最小的元素。

# 注意数组中可能存在重复的元素。

# 示例 1：

# 输入: [1,3,5]
# 输出: 1
# 示例 2：

# 输入: [2,2,2,0,1]
# 输出: 0
# 说明：

# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

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
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]


if __name__ == '__main__':

    nums = [2, 2, 2, 0, 1]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.findMin1(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
