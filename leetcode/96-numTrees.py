'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-25 12:01:21
'''

# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

# 示例:

# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[:2] = [1, 1]
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


if __name__ == '__main__':
    n = 3
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.numTrees(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
