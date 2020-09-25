'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-25 18:32:06
'''

# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

# 示例 1:

# 输入: "aacecaaa"
# 输出: "aaacecaaa"
# 示例 2:

# 输入: "abcd"
# 输出: "dcbabcd"

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 难， 不会
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        base, mod = 131, 10**9 + 7
        left = right = 0
        mul = 1
        best = -1

        for i in range(n):
            left = (left * base + ord(s[i])) % mod
            right = (right + mul * ord(s[i])) % mod
            if left == right:
                best = i
            mul = mul * base % mod

        add = ("" if best == n - 1 else s[best+1:])
        return add[::-1] + s


if __name__ == '__main__':
    s = "abcd"
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.shortestPalindrome(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
