'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-30 15:03:55
'''

# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

# 例如，从根到叶子节点路径 1->2->3 代表数字 123。

# 计算从根到叶子节点生成的所有数字之和。

# 说明: 叶子节点是指没有子节点的节点。

# 示例 1:

# 输入: [1,2,3]
#     1
#    / \
#   2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.
# 示例 2:

# 输入: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.

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
    # 递归
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = []

        def dfs(node, sum):
            if node:
                sum = sum * 10 + node.val
                if not node.left and not node.right:
                    # print(sum)
                    result.append(sum)
                if node.left:
                    dfs(node.left, sum)
                if node.right:
                    dfs(node.right, sum)
        dfs(root, 0)
        # print(sum(result))
        return sum(result)

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
    result = solution.sumNumbers1(root)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
