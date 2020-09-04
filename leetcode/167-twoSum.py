'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 16:12:33
'''

# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

# 说明:

# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:

# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def twoSum(self, numbers, target: int):
        length = len(numbers)
        if length < 2:
            return []
        left, right = 0, length - 1
        while left < right:
            ts = numbers[left] + numbers[right]
            if ts == target:
                return [left+1, right + 1]
            elif ts < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == '__main__':

    numbers = [2, 7, 11, 15]
    target = 9
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.twoSum(numbers, target)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
