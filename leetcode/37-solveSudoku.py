'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-19 16:31:49
'''
# 编写一个程序，通过已填充的空格来解决数独问题。

# 一个数独的解法需遵循如下规则：

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 空白格用 '.' 表示。

# 一个数独。
# 答案被标成红色。
# Note:

# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def solveSudoku(self, board) -> None:
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]

        empty = []
        for i in range(9):
            for j in range(9):
                pos = (i // 3) * 3 + j // 3
                if board[i][j] != '.':
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[pos].remove(val)
                else:
                    empty.append((i, j))

        # 迭代 empty数组就行了
        def backTrack(iter=0):
            if iter == len(empty):
                return True
            else:
                i, j = empty[iter]
                pos = (i // 3) * 3 + j // 3
                for num in row[i] & col[j] & block[pos]:
                    row[i].remove(num)
                    col[j].remove(num)
                    block[pos].remove(num)
                    board[i][j] = str(num)
                    if backTrack(iter+1):
                        return True
                    row[i].add(num)
                    col[j].add(num)
                    block[pos].add(num)
                return False
        backTrack()


if __name__ == '__main__':

    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    start_time = datetime.datetime.now()
    solution = Solution()
    solution.solveSudoku(board)
    print(board)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
