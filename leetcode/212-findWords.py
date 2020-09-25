'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-25 13:54:28
'''

# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

# 示例:

# 输入:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]

# 输出: ["eat","oath"]
# 说明:
# 你可以假设所有输入都由小写字母 a-z 组成。

# 提示:

# 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
# 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def findWords(self, board, words):
        result = []
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                if letter not in node.keys():
                    node[letter] = {}
                node = node[letter]
                # node = node.setdefault(letter, {})
            node["$"] = word

        R, C = len(board), len(board[0])

        def backTrack(row, col, parent):
            letter = board[row][col]
            curNode = parent[letter]

            word_math = curNode.pop("$", False)
            if word_math:
                result.append(word_math)

            board[row][col] = '#'
            directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for (x, y) in directs:
                newRow, newCol = row + x, col + y
                if newRow < 0 or newRow >= R or newCol < 0 or newCol >= C:
                    continue
                if not board[newRow][newCol] in curNode:
                    continue
                backTrack(newRow, newCol, curNode)

            board[row][col] = letter

            if not curNode:
                parent.pop(letter)

        for row in range(R):
            for col in range(C):
                if board[row][col] in trie:
                    backTrack(row, col, trie)

        return result


if __name__ == '__main__':
    words = ["oath", "pea", "eat", "rain", "ppe"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.findWords(board, words)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
