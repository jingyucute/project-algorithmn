'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-02 09:02:57
'''

# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

# 说明：

# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：

# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# 示例 2：

# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 示例 3：

# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 递归, 一如既往的超时
    def wordBreak(self, s: str, wordDict):
        result = []
        if not s or not wordDict:
            return result
        length = len(s)

        def checkWord(start, end, path):
            if start >= end:
                return
            if s[start:end] in wordDict:
                path.append(s[start:end])
                ans = ""
                for str in path:
                    ans += str + " "
                result.append(ans[0:-1])
                path.pop()
            for i in range(start, end):
                if s[start:i] in wordDict:
                    path.append(s[start:i])
                    checkWord(i, end, path)
                    path.pop()
        checkWord(0, length, [])
        return result

    def wordBreak1(self, s: str, wordDict):
        result = []
        if not s or not wordDict:
            return result

        map = {}

        def checkWord(ss):
            if ss in map:
                return map[ss]
            if not ss:
                return []
            path = []
            for word in wordDict:
                if not ss.startswith(word):
                    continue
                if len(word) == len(ss):
                    path.append(word)
                else:
                    rest = checkWord(ss[len(word):])
                    # print(rest)
                    for item in rest:
                        item = word + " " + item
                        path.append(item)
            map[ss] = path
            return path

        return checkWord(s)


if __name__ == '__main__':

    s = "catsanddog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.wordBreak1(s, wordDict)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
