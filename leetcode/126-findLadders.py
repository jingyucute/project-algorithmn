'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-30 12:39:06
'''

# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

# 每次转换只能改变一个字母。
# 转换后得到的单词必须是字典中的单词。
# 说明:

# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 示例 1:

# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# 输出:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# 示例 2:

# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# 输出: []

# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        result = []
        from collections import defaultdict

        wordId = defaultdict(int)
        idWord = []
        id = 0
        for word in wordList:
            if word not in wordId:
                wordId[word] = id
                id += 1
                idWord.append(word)

        if endWord not in wordId:
            return result

        if beginWord not in wordId:
            wordId[beginWord] = id
            id += 1
            idWord.append(beginWord)

        def checkTransform(word1, word2):
            diff = 0
            len1, len2 = len(word1), len(word2)
            if len1 != len2:
                return False

            for i in range(len1):
                if diff >= 2:
                    return False
                if word1[i] != word2[i]:
                    diff += 1
            return diff == 1

        word_counts = len(wordId)
        edges = [[] for _ in range(word_counts)]
        for i in range(word_counts - 1):
            for j in range(i+1, word_counts):
                if checkTransform(idWord[i], idWord[j]):
                    # 单词之间进行关系链接,
                    # print(idWord[i], idWord[j])
                    edges[i].append(j)
                    edges[j].append(i)

        dest = wordId[endWord]
        cost = [2**31] * word_counts
        queue = []
        tempBegin = []
        tempBegin.append(wordId[beginWord])
        queue.append(tempBegin)
        cost[wordId[beginWord]] = 0

        while queue:
            now = queue[0]
            del queue[0]
            last = now[-1]
            if last == dest:
                temp = [idWord[index] for index in now]
                result.append(temp[:])
            else:
                for i in range(len(edges[last])):
                    to = edges[last][i]
                    if cost[last] + 1 <= cost[to]:
                        cost[to] = cost[last] + 1
                        temp = now[:]
                        temp.append(to)
                        queue.append(temp)

        return result

    def findLadders1(self, beginWord: str, endWord: str, wordList):
        result = []
        se = set(wordList)
        if endWord not in se:
            return result

        marked = set()
        queue = [[beginWord]]

        def edges(word):
            arr = list(word)
            for i in range(len(arr)):
                c = arr[i]
                for j in range(97, 123):
                    arr[i] = chr(j)
                    newWord = ''.join(arr)
                    if newWord in se and not newWord in marked:
                        yield newWord
                arr[i] = c

        while queue:
            temp = []
            found = False
            for words in queue:
                marked.add(words[-1])
            for words in queue:
                for w in edges(words[-1]):
                    v = words + [w]
                    if w == endWord:
                        result.append(v)
                        found = True
                    temp.append(v)
            if found:
                break
            queue = temp
        return result

    # 不会 太难了
    def findLadders2(self, beginWord: str, endWord: str, wordList):
        import collections
        if not endWord in wordList:
            return []
        hash = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hash[word[:i]+"*"+word[i+1:]].append(word)

        def edges(word):
            for i in range(len(word)):
                for newWord in hash[word[:i]+'*'+word[i+1:]]:
                    if not newWord in marked:
                        yield newWord

        def findPath(end):
            res = []
            for curr in end:
                for parent in path[curr[0]]:
                    res.append([parent]+curr)
            return res
        marked = set()
        path = collections.defaultdict(set)
        begin = set([beginWord])
        end = set([endWord])
        forward = True
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
                forward = not forward
            temp = set()
            for word in begin:
                marked.add(word)
            for word in begin:
                for w in edges(word):
                    temp.add(w)
                    if forward:
                        path[w].add(word)
                    else:
                        path[word].add(w)
            begin = temp
            if begin & end:
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = findPath(res)
                return res
        return []


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.findLadders2(beginWord, endWord, wordList)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
