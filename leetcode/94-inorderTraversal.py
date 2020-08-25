'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-25 10:58:29
'''
# 给定一个二叉树，返回它的中序 遍历。

# 示例:

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [1,3,2]
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
    # LDR
    def inorderTraversal(self, root: TreeNode):
        result = []

        def inorder(node):
            if node:
                if node.left:
                    inorder(node.left)
                result.append(node.val)
                if node.right:
                    inorder(node.right)

        inorder(root)

        return result

    # 迭代
    def inorderTraversal1(self, root: TreeNode):
        result = []
        stack = []

        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result


if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.right = node1
    node1.left = node2
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.inorderTraversal1(root)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
