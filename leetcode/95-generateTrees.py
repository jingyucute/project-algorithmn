'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-25 11:47:23
'''

# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

#  

# 示例：

# 输入：3
# 输出：
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  

# 提示：

# 0 <= n <= 8


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    #  官方给的, 自己写点理解吧
    def generateTrees(self, n: int):
        def generateTrees(start, end):
            if start > end:
                return [None, ]
            allTrees = []
            for i in range(start, end+1):
                # 以 i 为当前结点, 两边扩展
                leftTrees = generateTrees(start, i - 1)
                rightTrees = generateTrees(i+1, end)
                for l in leftTrees:
                    for r in rightTrees:
                        curTree = TreeNode(i)
                        curTree.left = l
                        curTree.right = r
                        allTrees.append(curTree)

            return allTrees

        return generateTrees(1, n) if n else []


if __name__ == '__main__':
    n = 3
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.generateTrees(n)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
