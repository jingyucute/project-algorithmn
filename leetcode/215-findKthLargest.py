'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-25 18:50:27
'''
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 示例 1:

# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:

# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:

# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 暂时只想到快排， 先写写吧
    def findKthLargest(self, nums, k: int) -> int:
        length = len(nums)

        def findPrivot(low, high):
            privot = nums[low]
            while low < high:
                while low < high and nums[high] < privot:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] >= privot:
                    low += 1
                nums[high] = nums[low]
            nums[low] = privot
            return low

        def quickSort(low, high):
            if low < high:
                privot = findPrivot(low, high)
                quickSort(low, privot - 1)
                quickSort(privot+1, high)

        quickSort(0, length - 1)
        return nums[k - 1]

    # 其他方法
    def findKthLargest1(self, nums, k: int) -> int:
        return 0


if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.findKthLargest(nums, k)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
