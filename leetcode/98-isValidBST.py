'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-25 12:49:42
'''

# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

# 假设一个二叉搜索树具有如下特征：

# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:

# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:

# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = []

        def inorder(root):
            if root:
                if root.left:
                    inorder(root.left)
                result.append(root.val)
                if root.right:
                    inorder(root.right)
        inorder(root)

        for i in range(1, len(result)):
            if result[i] <= result[i - 1]:
                return False

        return True


if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.right = node1
    node1.left = node2
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.isValidBST(root)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
