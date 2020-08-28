'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 12:15:45
'''

# 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

# 一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

# 题目数据保证答案符合 32 位带符号整数范围。

#  

# 示例 1：

# 输入：S = "rabbbit", T = "rabbit"
# 输出：3
# 解释：

# 如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)

# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 示例 2：

# 输入：S = "babgbag", T = "bag"
# 输出：5
# 解释：

# 如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。
# (上箭头符号 ^ 表示选取的字母)

# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    #  动态规划
    def numDistinct(self, s: str, t: str) -> int:

        lens, lent = len(s), len(t)

        dp = [[0] * (lent + 1) for _ in range(lens + 1)]

        for i in range(lens + 1):
            dp[i][0] = 1  # 若t为空串, 方案为1
        for i in range(1, lens + 1):
            for j in range(1, lent + 1):
                # dp[i][j] s中前i个字符 t中前j个字符 组成的方案
                if s[i - 1] == t[j - 1]:
                    # 第 i 个字符 和 第 j 个字符相等
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        # print(dp)
        return dp[lens][lent]


if __name__ == '__main__':
    s = 'babgbag'
    t = "bag"
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.numDistinct(s, t)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
