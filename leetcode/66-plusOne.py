'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 14:48:38
'''
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例 1:

# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:

# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def plusOne(self, digits):
        length = len(digits)
        add = 1
        for i in range(length - 1, -1, -1):
            cur_num = digits[i]
            digits[i] = (cur_num + add) % 10
            add = (cur_num + add) // 10
        if add == 1:
            digits = [add] + digits
        return digits


if __name__ == '__main__':
    digits = [9]
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.plusOne(digits)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
