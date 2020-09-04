'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 17:00:36
'''

# 给定一个Excel表格中的列名称，返回其相应的列序号。

# 例如，

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# 示例 1:

# 输入: "A"
# 输出: 1
# 示例 2:

# 输入: "AB"
# 输出: 28
# 示例 3:

# 输入: "ZY"
# 输出: 701

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def titleToNumber(self, s: str) -> int:
        # if not s:
        #     return 0
        # d = {

        # }
        # for i in range(26):
        #     char = chr(65 + i)
        #     d[char] = i + 1
        # res = 0
        # for letter in s:
        #     res = res * 26 + d[letter]
        # return res

        res = 0
        for letter in s:
            num = ord(letter) + 1 - ord('A')
            res = res * 26 + num
        return res


if __name__ == '__main__':

    s = "ZZ"

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.titleToNumber(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
