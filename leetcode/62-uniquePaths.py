'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 11:28:30
'''

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

# 问总共有多少条不同的路径？


# 例如，上图是一个 7 x 3 的网格。有多少可能的路径？ 

# 示例 1:

# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 示例 2:

# 输入: m = 7, n = 3
# 输出: 28
#  

# 提示：

# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 10 ^ 9


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划
        # m col   n row
        map = [[0] * m for _ in range(n)]
        map[0][0] = 1
        for row in range(n):
            for col in range(m):
                if row == 0 and col == 0:
                    map[row][col] = 1
                elif row == 0 and col != 0:
                    map[row][col] = map[row][col - 1]
                elif row != 0 and col == 0:
                    map[row][col] = map[row-1][col]
                elif row != 0 and col != 0:
                    map[row][col] = map[row-1][col] + map[row][col - 1]

        return map[n-1][m-1]

    # 看到的一个很牛皮的想法
    # 组合数, 因为从 [0, 0] -> [n-1, m -1] 一共会走 m + n -2步
    # 其中 有 n - 1步是向下的， m - 1 步向右的
    # C m n = m ! / (n! (m - n)!)
    def uniquePaths1(self, m: int, n: int) -> int:
        import math
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))


if __name__ == '__main__':
    m = 7
    n = 3
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.uniquePaths1(m, n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
