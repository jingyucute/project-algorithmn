'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 10:23:52
'''

# 在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。

# 如果存在则返回 true，不存在返回 false。

#  

# 示例 1:

# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true
# 示例 2:

# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true
# 示例 3:

# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 暂时没思路， 暴力试试 ,必然超时
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        length = len(nums)
        for i in range(length):
            for j in range(1, k + 1):
                if i + j >= length:
                    continue
                if abs(nums[i + j] - nums[i]) <= t:
                    return True
        return False

    # 参考官方的 分桶
    def containsNearbyAlmostDuplicate1(self, nums, k: int, t: int) -> bool:
        bucket = dict()
        length = len(nums)
        for i in range(length):
            nth = nums[i] // (t + 1)
            if nth in bucket:
                return True
            if (nth - 1) in bucket and abs(nums[i] - bucket[nth - 1]) <= t:
                return True
            if (nth + 1) in bucket and abs(nums[i] - bucket[nth + 1]) <= t:
                return True
            bucket[nth] = nums[i]
            if i >= k:
                bucket.pop(nums[i - k] // (t + 1))
        return False


if __name__ == '__main__':

    nums = [2147483646, 2147483647]
    k = 3
    t = 3
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.containsNearbyAlmostDuplicate1(nums, k, t)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
