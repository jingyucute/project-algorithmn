'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 10:21:03
'''
# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# 说明: 叶子节点是指没有子节点的节点。

# 示例:

# 给定二叉树 [3, 9, 20, null, null, 15, 7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.

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
    def minDepth(self, root: TreeNode) -> int:
        def height(node):
            if not node:
                return 0
            if not node.left:
                return height(node.right) + 1
            if not node.right:
                return height(node.left) + 1
            lh = height(node.left)
            rh = height(node.right)
            return min(lh, rh) + 1
        return height(root)

    def broadTravse(self, root):
        result = []
        if not root:
            return result
        queue = []
        queue.append(root)
        while queue:
            length = len(queue)
            temp = []
            for _ in range(length):
                node = queue[0]
                del queue[0]
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(temp[:])
        return result


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
    result = solution.minDepth(root)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
