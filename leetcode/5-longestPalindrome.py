'''
Description: 
Author: jingyu
Date: 2020-08-08 00:26:08
LastEditors: Please set LastEditors
LastEditTime: 2020-08-09 23:09:37
'''
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：

# 输入: "cbbd"
# 输出: "bb"

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    # 中心扩展  选取一个对称中心， 向两边扩展，求出最大回文数
    def longestPalindrome2(self, s: str) -> str:
        #
        length = len(s)
        start, end = 0, 0
        for i in range(length):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i+1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end+1]

    # 动态规划

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        list = [[False for j in range(
            length)] for i in range(length)]
        # list[i][j] 表示 str中的下表i->j的字符串是否为回文数

        result = ""
        for d in range(0, length):  # 规模 从 1个回文 -> n
            for i in range(0, length - d):
                # 从 0 开始填, 直到 n - d - 1
                j = i + d
                if d == 0:
                    list[i][j] = True
                elif d == 1:
                    if s[i] == s[j]:
                        list[i][j] = True
                else:
                    if list[i+1][j-1] and s[i] == s[j]:
                        list[i][j] = True
                if list[i][j] and j - i + 1 > len(result):
                    result = s[i:j+1]
        return result

    # 暴力算法

    def longestPalindrome1(self, s: str) -> str:
        # 暴力解法， 超出时间限制
        def checkStr(ss):
            left = 0
            right = len(ss) - 1
            flag = True
            while left < right:
                if ss[left] == ss[right]:
                    left += 1
                    right -= 1
                    continue
                else:
                    flag = False
                    break
            return flag

        i = 0
        j = len(s)
        result_temp = ""
        while i < len(s):
            while j > i:
                temp = s[i:j]
                if checkStr(temp) and len(temp) > len(result_temp):
                    result_temp = temp
                j -= 1
            i += 1
            j = len(s)
        return result_temp


if __name__ == '__main__':
    str = 'a'
    start_time = datetime.datetime.now()
    s = Solution()
    result = s.longestPalindrome2(str)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
