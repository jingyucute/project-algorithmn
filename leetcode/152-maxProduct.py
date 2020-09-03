'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-03 19:21:34
'''

# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

#  

# 示例 1:

# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:

# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def maxProduct(self, nums) -> int:
        if not nums:
            return 0
        length = len(nums)
        maxDp = [nums[0]] * length
        minDp = [nums[0]] * length
        for i in range(1, length):
            maxDp[i] = max(nums[i], max(maxDp[i - 1] *
                                        nums[i], minDp[i - 1] * nums[i]))
            minDp[i] = min(nums[i], min(maxDp[i - 1] *
                                        nums[i], minDp[i - 1] * nums[i]))

        return max(maxDp)


if __name__ == '__main__':

    nums = [2, 3, -2, 4]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.maxProduct(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
