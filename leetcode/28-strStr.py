'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-15 08:25:44
'''
# 实现 strStr() 函数。

# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

# 示例 1:

# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:

# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 说明:

# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:

    # 暴力匹配
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(haystack), len(needle)

        for i in range(L - n + 1):
            if haystack[i:i+n] == needle:
                return i

        return -1

    # 官方双指针
    # 我看咱还是暴力呢
    def strStr1(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L == 0:
            return 0

        pn = 0
        while pn < n - L + 1:
            # find the position of the first needle character
            # in the haystack string
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1

            # compute the max match string
            curr_len = pL = 0
            while pL < L and pn < n and haystack[pn] == needle[pL]:
                pn += 1
                pL += 1
                curr_len += 1

            # if the whole needle string is found,
            # return its start position
            if curr_len == L:
                return pn - L

            # otherwise, backtrack
            pn = pn - curr_len + 1

        return -1

    # KMP 算法， 不会了， 后面再写吧


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    start_time = datetime.datetime.now()
    solution = Solution()
    r = solution.strStr(haystack, needle)
    print(r)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
