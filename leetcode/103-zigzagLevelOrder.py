'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-27 19:33:04
'''

# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：

# [
#   [3],
#   [20,9],
#   [15,7]
# ]


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    #  层次遍历
    def zigzagLevelOrder(self, root: TreeNode):
        result = []
        if not root:
            return result

        queue = []
        queue.append(root)

        direct = 0  # 0 当前层从左往右 1 从右往左
        while queue:
            length = len(queue)
            temp = []
            queue[:] = queue[::-1]
            for _ in range(length):
                node = queue[0]
                del queue[0]
                temp.append(node.val)
                if direct == 0:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if direct == 1:

                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)

            result.append(temp[:])
            direct = (direct + 1) % 2

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
    result = solution.zigzagLevelOrder(root)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
