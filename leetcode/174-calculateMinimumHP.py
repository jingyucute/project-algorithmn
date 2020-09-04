'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 19:32:25
'''

# 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。

# 为了尽快到达公主，骑士决定每次只向右或向下移动一步。

#  

# 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。

# 例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。

# -2 (K)	-3	3
# -5	-10	1
# 10	30	-5 (P)
#  

# 说明:

# 骑士的健康点数没有上限。

# 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    # 本地转为化求左上角到右下角所需要的最小健康值
    # 写了一半， 不会了, 然后看了一下答案
    def calculateMinimumHP(self, dungeon) -> int:
        if not dungeon or not dungeon[0]:
            return 0
        R, C = len(dungeon), len(dungeon[0])

        dp = [[10**9] * (C + 1) for _ in range(R + 1)]
        dp[R][C-1] = dp[R-1][C] = 1
        for i in range(R-1, - 1, -1):
            for j in range(C - 1, -1, -1):
                minH = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, minH - dungeon[i][j])

        return dp[0][0]


if __name__ == '__main__':

    dungeon = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5],
    ]

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.calculateMinimumHP(dungeon)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
