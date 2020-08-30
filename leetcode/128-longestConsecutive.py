'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-30 14:09:43
'''

# 给定一个未排序的整数数组，找出最长连续序列的长度。

# 要求算法的时间复杂度为 O(n)。

# 示例:

# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        long_streak = 0
        for num in nums:
            if num - 1 not in nums_set:
                cur_num = num
                cur_streak = 1
                while cur_num + 1 in nums_set:
                    cur_num += 1
                    cur_streak += 1
                long_streak = max(long_streak, cur_streak)
        return long_streak


if __name__ == '__main__':
    nums = []

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.longestConsecutive(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
