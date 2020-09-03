'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-03 11:08:27
'''

# 给定一个二叉树，返回它的 后序 遍历。

# 示例:

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [3,2,1]
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
    def postorderTraversal(self, root: TreeNode):
        result = []

        def postorder(node):
            if node:
                if node.left:
                    postorder(node.left)
                if node.right:
                    postorder(node.right)
                result.append(node.val)
        postorder(root)
        return result

    # 单栈
    def postorderTraversal1(self, root: TreeNode):
        result = []
        if not root:
            return result
        stack = []
        cur = root
        pre = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            if stack:
                cur = stack.pop()
                if not cur.right or pre == cur.right:
                    # 当前结点没有右孩子 或者已经访问过右孩子
                    result.append(cur.val)
                    pre = cur
                    cur = None
                else:
                    # 有右孩子 且 右孩子没有访问过
                    # 继续访问右孩子
                    stack.append(cur)
                    cur = cur.right

        return result

    #  LRD -> DRL 将跟右左的结果进行反序, 就是后续遍历的结果


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
    result = solution.postorderTraversal1(root)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
