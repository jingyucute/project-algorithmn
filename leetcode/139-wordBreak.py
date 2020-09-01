'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-01 15:58:11
'''

# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

# 说明：

# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：

# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：

# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：

# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 递归, 我丢, 超时
    def wordBreak(self, s: str, wordDict) -> bool:
        if not s or not wordDict:
            return False

        length = len(s)

        def checkWord(start, end):
            if start >= end:
                return False
            if s[start:end] in wordDict:
                return True
            for i in range(start, end):
                if s[start:i] in wordDict:
                    if checkWord(i, end):
                        return True
                else:
                    continue
            return False

        return checkWord(0, length)

    # dp
    def wordBreak1(self, s: str, wordDict) -> bool:
        if not s or not wordDict:
            return False
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True
        for i in range(1, length + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[length]


if __name__ == '__main__':

    s = "applepenapple"
    wordDict = ["apple", "pen"]

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.wordBreak1(s, wordDict)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
