'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-10-03 09:59:06
'''

""" 根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

 

示例：

输入： 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出：
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
 

进阶：

你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/game-of-life
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 """




import datetime
class Solution:
    def gameOfLife(self, board) -> None:
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        directs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                   (0, 1), (1, -1), (1, 0), (1, 1)]

        d = {

        }

        for row in range(R):
            for col in range(C):
                alive_count = 0
                death_count = 0
                for (x, y) in directs:
                    new_row, new_col = row + x, col + y
                    if new_row < 0 or new_row >= R or new_col < 0 or new_col >= C:
                        continue
                    else:
                        # print((row, col), (x, y), (new_row, new_col))
                        if board[new_row][new_col] == 0:
                            death_count += 1
                        else:
                            alive_count += 1

                # print((row, col), alive_count, death_count)

                if board[row][col] == 1:
                    # 当前是活细胞
                    if alive_count < 2 or alive_count > 3:
                        # 周围活细胞小于2
                        d[(row, col)] = 0
                else:
                    # 当前是死细胞
                    if alive_count == 3:
                        d[(row, col)] = 1

        for (row, col), v in d.items():
            board[row][col] = v


if __name__ == '__main__':
    board = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
    ]
    solution = Solution()
    start_time = datetime.datetime.now()
    solution.gameOfLife(board)
    print(board)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
