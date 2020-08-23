'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-23 14:27:05
'''

# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

#  

# 示例:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#  

# 提示：

# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def exist(self, board, word: str) -> bool:
        if not board or not board[0] or len(word) == 0:
            return False
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R, C = len(board), len(board[0])
        status = [[0] * C for _ in range(R)]

        def backTrack(i, j, status, word):
            if len(word) == 0:
                return True
            for direct in directs:
                cur_i, cur_j = i + direct[0], j + direct[1]
                if cur_i >= 0 and cur_i < R and cur_j >= 0 and cur_j < C and board[cur_i][cur_j] == word[0]:
                    if status[cur_i][cur_j] == 1:
                        continue
                    status[cur_i][cur_j] = 1
                    if backTrack(cur_i, cur_j, status, word[1:]):
                        return True
                    else:
                        status[cur_i][cur_j] = 0
            return False

        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    status[i][j] = 1
                    # dfs
                    if backTrack(i, j, status, word[1:]):
                        return True
                    else:
                        # 回溯
                        status[i][j] = 0

        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCB'
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.exist(board, word)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
