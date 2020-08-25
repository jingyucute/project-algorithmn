'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-25 16:04:07
'''

# 给定两个二叉树，编写一个函数来检验它们是否相同。

# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

# 示例 1:

# 输入:       1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# 输出: true
# 示例 2:

# 输入:      1          1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# 输出: false
# 示例 3:

# 输入:       1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# 输出: false

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        return True


if __name__ == '__main__':
    p = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    p.right = node1
    node1.left = node2

    q = TreeNode(1)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    q.right = node3
    node3.left = node4
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.isSameTree(p, q)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
