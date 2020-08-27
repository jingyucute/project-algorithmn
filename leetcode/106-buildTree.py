'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 00:54:27
'''

# 根据一棵树的中序遍历与后序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 例如，给出

# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：

#     3
#    / \
#   9  20
#     /  \
#    15   7

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
    def buildTree(self, inorder, postorder) -> TreeNode:
        if not postorder:
            return None
        node_val = postorder[-1]
        node_index = inorder.index(node_val)

        node_left = self.buildTree(
            inorder[0:node_index], postorder[0:node_index])

        node_right = self.buildTree(
            inorder[node_index + 1:], postorder[node_index:-1])
        node = TreeNode(node_val)
        node.left = node_left
        node.right = node_right
        return node


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

    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    start_time = datetime.datetime.now()
    solution = Solution()
    root = solution.buildTree(inorder, postorder)
    print(root.val)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
