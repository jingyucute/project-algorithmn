'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-31 15:33:45
'''

# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 说明：

# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

# 示例 1:

# 输入: [2,2,1]
# 输出: 1
# 示例 2:

# 输入: [4,1,2,1,2]
# 输出: 4

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:

    def singleNumber(self, nums) -> int:
        # from collections import defaultdict
        # d = defaultdict(int)
        # for num in nums:
        #     if num not in d:
        #         d[num] = 1
        #     else:
        #         d[num] += 1
        # for k, v in d.items():
        #     if v == 1:
        #         return k
        # return -1

        se = set()
        for num in nums:
            if num not in se:
                se.add(num)
            else:
                se.remove(num)
        return se.pop()

    def singleNumber1(self, nums) -> int:
        # 异或运算
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':

    nums = [1, 3, 3, 4, 4]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.singleNumber(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
