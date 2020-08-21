'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 10:27:47
'''

# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。

# 说明:

# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
# 示例 1:

# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:

# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 示例 3:

# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 示例 4:

# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 示例 5:

# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输出: false


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        m, n = len(s), len(p)

        list = [[False] * (n + 1) for _ in range(m + 1)]

        list[0][0] = True
        if p[0] == '*':
            list[0][1] = True

        def checkMatch(i, j):
            if i == 0:
                return False
            if p[j - 1] == '?':
                return True
            return s[i - 1] == p[j - 1]

        # for i in range(1, n + 1):
        #     if p[i - 1] == '*':
        #         list[0][i] = True
        #     else:
        #         break
        # print(list)

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j - 1] == '*':
                    if list[i][j - 1] or list[i - 1][j]:
                        list[i][j] = True
                else:
                    if checkMatch(i, j):
                        list[i][j] = list[i - 1][j - 1]
        print(list)
        return list[m][n]


if __name__ == '__main__':

    s = "adceb"
    p = "*a*b"
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.isMatch(s, p)
    print(result)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
