'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 16:01:23
'''

# 翻转一棵二叉树。

# 示例：

# 输入：

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# 备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：

# 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/invert-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

    def traverse(self, node):
        if node:
            print(node.val)
            self.traverse(node.left)
            self.traverse(node.right)


if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    solution = Solution()
    start_time = datetime.datetime.now()
    node = solution.invertTree(root)
    solution.traverse(node)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
