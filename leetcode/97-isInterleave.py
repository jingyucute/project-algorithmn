'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-25 12:38:17
'''

# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

#  

# 示例 1：

# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true
# 示例 2：

# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len1 + len2 != len3:
            return False

        # dp[len1][len2]
        # dp[i][j] 表示s1中前i个字符 和 s2中前j个字符 能否组成 s3中前 i+j个字符
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = True  # 两个空串自然可以
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i - 1]

        for j in range(1, len2 + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j - 1]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]
                            ) or (dp[i][j-1] and s2[j-1] == s3[i+j - 1])
        return dp[len1][len2]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.isInterleave(s1, s2, s3)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
