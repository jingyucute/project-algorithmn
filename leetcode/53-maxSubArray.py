'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 19:24:00
'''

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:

# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    # 暴力算法
    # 超时
    def maxSubArray(self, nums) -> int:
        length = len(nums)
        max_sum = -2**31
        for guimo in range(length, 0, -1):
            # print(guimo)
            for start in range(0, length - guimo + 1):
                # length-1 - start + 1 >= guomo
                end = start + guimo - 1
                temp_sum = 0
                for i in range(start, end + 1):
                    temp_sum += nums[i]
                if temp_sum > max_sum:
                    max_sum = temp_sum

        return max_sum

    # 动态规划
    def maxSubArray1(self, nums) -> int:
        # dp[i] = max(dp[i - 1] + a[i], a[i])
        max_sum = nums[0]
        pre = 0  # 前面最大的
        for num in nums:
            pre = max(pre + num, num)
            max_sum = max(max_sum, pre)
        return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.maxSubArray1(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
