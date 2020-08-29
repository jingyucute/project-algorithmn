'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-29 16:13:09
'''

# 给定一个非空二叉树，返回其最大路径和。

# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

# 示例 1:

# 输入: [1,2,3]

#        1
#       / \
#      2   3

# 输出: 6
# 示例 2:

# 输入: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# 输出: 42

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def maxPath(node, result):
            if not node:
                return 0
            left = max(maxPath(node.left, result), 0)
            right = max(maxPath(node.right, result), 0)

            val = left + right + node.val
            result[0] = max(result[0], val)
            return node.val + max(left, right)
        max_Sum = -2**30
        result = [
            max_Sum
        ]
        maxPath(root, result)
        return result[0]


if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(5)
    node1_1 = TreeNode(3)
    node1_2 = TreeNode(4)
    node2_1 = TreeNode(4)
    node2_2 = TreeNode(3)
    root.left = node1
    root.right = node2
    node1.left = node1_1
    node1.right = node1_2
    node2.left = node2_1
    node2.right = node2_2

    head = ListNode(-10)
    lnode1 = ListNode(-3)
    lnode2 = ListNode(0)
    lnode3 = ListNode(5)
    lnode4 = ListNode(9)
    head.next = lnode1
    lnode1.next = lnode2
    lnode2.next = lnode3
    lnode3.next = lnode4

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.maxPathSum(root)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
