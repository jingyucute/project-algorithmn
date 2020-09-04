'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 16:46:00
'''

# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

#  

# 示例 1:

# 输入: [3,2,3]
# 输出: 3
# 示例 2:

# 输入: [2,2,1,1,1,2,2]
# 输出: 2

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def majorityElement(self, nums) -> int:
        # if not nums:
        #     return 0
        # d = {

        # }
        # for num in nums:
        #     if num not in d:
        #         d[num] = 1
        #     else:
        #         d[num] += 1
        # more_count, more_num = 1, nums[0]
        # for k, v in d.items():
        #     if v > more_count:
        #         more_count = v
        #         more_num = k
        # return more_num
        from collections import Counter
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement1(self, nums) -> int:
        if not nums:
            return 0
        nums.sort()
        length = len(nums)
        return nums[length // 2]


if __name__ == '__main__':

    nums = [2, 2, 1, 1, 1, 2, 2]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.majorityElement(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
