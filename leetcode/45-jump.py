'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 11:02:18
'''

# 给定一个非负整数数组，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。

# 示例:

# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 说明:

# 假设你总是可以到达数组的最后一个位置。

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:

    def jump(self, nums) -> int:
        n = len(nums)
        maxPos = 0
        end = 0
        step = 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
            print(i, maxPos, end, step)
        return step


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.jump(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
