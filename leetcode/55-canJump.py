'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 20:10:39
'''

# 给定一个非负整数数组，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个位置。

# 示例 1:

# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 示例 2:

# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    # 贪心算法
    def canJump(self, nums) -> bool:
        length = len(nums)
        maxPos = 0
        for i in range(length):
            if i <= maxPos:
                # 最大位置 和 当前位置加上最大步数后的新位置
                maxPos = max(maxPos, i + nums[i])
                if maxPos >= length - 1:
                    return True
            else:
                break
        return False


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.canJump(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
