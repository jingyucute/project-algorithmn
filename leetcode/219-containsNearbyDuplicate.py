'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 09:31:25
'''

# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

#  

# 示例 1:

# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 示例 2:

# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 示例 3:

# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        import collections
        d = collections.defaultdict(list)

        for i, num in enumerate(nums):
            if num not in d:
                d[num].append(i)
            else:
                if i - d[num][-1] <= k:
                    return True
                else:
                    d[num].append(i)

        return False


if __name__ == '__main__':

    nums = [1, 0, 1, 1]
    k = 1
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.containsNearbyDuplicate(nums, k)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
