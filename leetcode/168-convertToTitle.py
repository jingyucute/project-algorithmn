'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 16:32:44
'''

# 给定一个正整数，返回它在 Excel 表中相对应的列名称。

# 例如，

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
# 示例 1:

# 输入: 1
# 输出: "A"
# 示例 2:

# 输入: 28
# 输出: "AB"
# 示例 3:

# 输入: 701
# 输出: "ZY"

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def convertToTitle(self, n: int) -> str:
        wl = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = []
        while n:
            n -= 1
            result.append(n % 26)
            n = n // 26
        res = ''
        for i in range(len(result) - 1, -1, -1):
            res += wl[result[i]]
        return res


if __name__ == '__main__':

    n = 27
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.convertToTitle(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
