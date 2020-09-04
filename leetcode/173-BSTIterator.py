'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 17:31:50
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


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.current_index = -1
        self.sort_node = []

        def inorder(node):
            if node:
                if node.left:
                    inorder(node.left)
                self.sort_node.append(node.val)
                if node.right:
                    inorder(node.right)
        inorder(root)
        self.total_length = len(self.sort_node)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.current_index += 1
        return self.sort_node[self.current_index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.current_index + 1 <= self.total_length:
            return True
        else:
            return False


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
    solution = BSTIterator(root)
    result = solution.next()
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
