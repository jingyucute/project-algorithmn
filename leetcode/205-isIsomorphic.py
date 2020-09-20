'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-20 17:55:47
'''

# 给定两个字符串 s 和 t，判断它们是否是同构的。

# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

# 示例 1:

# 输入: s = "egg", t = "add"
# 输出: true
# 示例 2:

# 输入: s = "foo", t = "bar"
# 输出: false
# 示例 3:

# 输入: s = "paper", t = "title"
# 输出: true
# 说明:
# 你可以假设 s 和 t 具有相同的长度。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            else:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
        return True


if __name__ == '__main__':

    s = "paper"
    t = "title"
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.isIsomorphic(s, t)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
