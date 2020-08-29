'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-29 17:08:05
'''

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。

# 示例 1:

# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:

# 输入: "race a car"
# 输出: false

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join((ch.lower() for ch in s if ch.isalnum()))
        # return ss == ss[::-1]
        left, right = 0, len(ss) - 1
        while left <= right:
            if ss[left] == ss[right]:
                left, right = left + 1, right - 1
            else:
                return False
        return True


if __name__ == '__main__':
    s = "."
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.isPalindrome(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
