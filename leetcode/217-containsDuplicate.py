'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-25 19:11:10
'''

# 给定一个整数数组，判断是否存在重复元素。

# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

#  

# 示例 1:

# 输入: [1,2,3,1]
# 输出: true
# 示例 2:

# 输入: [1,2,3,4]
# 输出: false
# 示例 3:

# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def containsDuplicate(self, nums) -> bool:
        uq = set()
        for num in nums:
            if num not in uq:
                uq.add(num)
            else:
                return True
        return False


if __name__ == '__main__':

    nums = [1, 2, 3, 4]
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.containsDuplicate(nums)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
