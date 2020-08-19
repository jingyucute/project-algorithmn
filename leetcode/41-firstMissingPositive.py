'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-19 19:17:46
'''


# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

#  

# 示例 1:

# 输入: [1,2,0]
# 输出: 3
# 示例 2:

# 输入: [3,4,-1,1]
# 输出: 2
# 示例 3:

# 输入: [7,8,9,11,12]
# 输出: 1


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def firstMissingPositive(self, nums) -> int:
        # 只需要标记 nums中 是否有 1 -> length 的数据
        length = len(nums)
        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1

        for i in range(length):
            num = abs(nums[i])
            if num <= length:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(length):
            if nums[i] > 0:
                return i + 1

        return length + 1


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    solution = Solution()

    nums = [3, 4, -1, 1]
    result = solution.firstMissingPositive(nums)
    print(result)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
