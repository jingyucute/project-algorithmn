'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-03 09:06:56
'''

# 给定一个二叉树，返回它的 前序 遍历。

#  示例:

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [1,2,3]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def preorderTraversal(self, root: TreeNode):
        result = []

        def preorder(node):
            if node:

                result.append(node.val)
                if node.left:
                    preorder(node.left)
                if node.right:
                    preorder(node.right)
        preorder(root)
        return result

    # 这个方法是看的别人的
    def preorderTraversal1(self, root: TreeNode):
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return result

    def preorderTraversal2(self, root: TreeNode):
        result = []
        if not root:
            return result
        stack = []
        node = root
        while node or stack:
            while node:
                result.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

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

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.preorderTraversal2(root)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
