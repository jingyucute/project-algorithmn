'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-30 23:59:23
'''

# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

# 返回 s 所有可能的分割方案。

# 示例:

# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:

    def partition(self, s: str):
        # 回溯法
        # 如果前面一部分可以回文, 则后面部分进行递归
        result = []
        if not s:
            return result
        length = len(s)

        def checkPalindrome(left, right):

            while left < right:
                if s[left] == s[right]:
                    left, right = left + 1, right - 1
                else:
                    return False
            return True

        def backTrack(start, len, path):
            if start == len:
                result.append(path[:])
            else:
                for i in range(start, len):
                    if not checkPalindrome(start, i):
                        continue
                    path.append(s[start:i+1])
                    backTrack(i+1, len, path)
                    path.pop()

        backTrack(0, length, [])
        return result

    def partition1(self, s: str):
        # 打表, 将判断回文的结果记录下来
        result = []
        if not s:
            return result
        length = len(s)
        dp = [[False] * length for _ in range(length)]
        for right in range(length):
            for left in range(0, right+1):
                if s[left] == s[right] and (right - left <= 2 or dp[left+1][right-1]):
                    dp[left][right] = True

        def backTrack(start, len, path):
            if start == len:
                result.append(path.copy())
            else:
                for i in range(start, len):
                    if not dp[start][i]:
                        continue
                    path.append(s[start:i+1])
                    backTrack(i+1, len, path)
                    path.pop()

        backTrack(0, length, [])

        return result


if __name__ == '__main__':

    s = "abbab"
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.partition1(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
