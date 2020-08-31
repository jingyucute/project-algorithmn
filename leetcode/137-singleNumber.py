'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-31 16:00:05
'''

# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

# 说明：

# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

# 示例 1:

# 输入: [2,2,3,2]
# 输出: 3
# 示例 2:

# 输入: [0,1,0,1,0,1,99]
# 输出: 99

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:

    def singleNumber(self, nums) -> int:

        # return (3*sum(set(nums)) - sum(nums)) // 2
        from collections import Counter
        map = Counter(nums)
        for k, v in map.items():
            if v == 1:
                return k
        return -1

    def singleNumber1(self, nums) -> int:
        # 异或运算
        seen_once = seen_twice = 0

        for num in nums:
            # first appearance:
            # add num to seen_once
            # don't add to seen_twice because of presence in seen_once

            # second appearance:
            # remove num from seen_once
            # add num to seen_twice

            # third appearance:
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once


if __name__ == '__main__':

    nums = [2, 2, 3, 2]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.singleNumber1(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
