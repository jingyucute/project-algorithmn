'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-30 15:34:19
'''

# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

# 示例:

# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：

# X X X X
# X X X X
# X X X X
# X O X X
# 解释:

# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def solve(self, board) -> None:
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])

        directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # 从边界出发， 如果边界上有 O , 再扩散

        def dfs(row, col):
            if not 0 <= row < R or not 0 <= col < C or board[row][col] != 'O':
                return
            board[row][col] = "A"
            temp = (row, col)
            for direct in directs:
                row += direct[0]
                col += direct[1]
                dfs(row, col)
                (row, col) = temp

        for row in range(R):
            dfs(row, 0)
            dfs(row, C-1)

        for col in range(C):
            dfs(0, col)
            dfs(R-1, col)

        for row in range(R):
            for col in range(C):
                if board[row][col] == "A":
                    board[row][col] = "O"
                elif board[row][col] == 'O':
                    board[row][col] = "X"


if __name__ == '__main__':

    board = [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]
    ]
    start_time = datetime.datetime.now()
    solution = Solution()
    solution.solve(board)
    print(board)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
