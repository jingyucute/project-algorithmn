'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-21 18:21:57
'''


# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。


# 上图为 8 皇后问题的一种解法。

# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

# 示例:

# 输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  

# 提示：

# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自 百度百科 - 皇后 ）


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def solveNQueens(self, n: int):
        list = [0] * (n + 1)
        result = []

        def check(index):
            for i in range(1, index):
                if list[index] == list[i] or abs(index - i) == abs(list[index] - list[i]):
                    return False
            return True

        def backTrack(index):
            if index > n:
                ans = [

                ]
                for i in range(1, n + 1):
                    choice = ''
                    cur = list[i]
                    for j in range(n):
                        if j == cur - 1:
                            choice += 'Q'
                        else:
                            choice += '.'
                    ans.append(choice)
                result.append(ans)
            else:
                for i in range(1, n + 1):
                    list[index] = i
                    if check(index):
                        backTrack(index + 1)
        backTrack(1)
        return result


if __name__ == '__main__':
    n = 4
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.solveNQueens(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
