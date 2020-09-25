'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-25 14:30:15
'''

# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

# 示例 1:

# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 示例 2:

# 输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def rob(self, nums) -> int:
        # 可不可以分成两部分 0 -> n-2 , 1 -> n -1
        if not nums:
            return 0

        length = len(nums)

        if length <= 3:
            return max(nums)

        def getMax(nl):
            n = len(nl)
            dp = [0] * n
            dp[0] = nl[0]
            for i in range(1, n):
                dp[i] = max(dp[i-1], dp[i - 2] + nl[i])

            return dp[-1]

        l1, l2 = getMax(nums[0:length - 1]), getMax(nums[1:length])

        return max(l1, l2)


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.rob(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
