'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-17 10:43:42
'''

# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须原地修改，只允许使用额外常数空间。

# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime

# 先粘过来， 这个没太看懂


class Solution:
    def nextPermutation(self, nums):
        # 找到 nums[i] < nums[i + 1]
        # 然后从 length-1 -> i+1 中找到 nums[j] > nums[i] 中的 第一个 j, 这个一定找得到
        # 交换 nums[i]和nums[j], 然后 剩下的 i + 1 到 length -1 中 反序排列， 因为找的是字典顺序
        def reverse(nums, start):
            end = len(nums) - 1
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1

        length = len(nums)
        if length <= 1:
            return

        i = length - 2

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = length - 1
            while i < j and nums[i] >= nums[j]:
                j -= 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        reverse(nums, i+1)


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()

    nums = [1, 2, 3]
    nums = [1, 3, 2]

    solution.nextPermutation(nums)
    print(nums)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
