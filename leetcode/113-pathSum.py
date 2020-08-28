'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 11:36:38
'''

# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

# 说明: 叶子节点是指没有子节点的节点。

# 示例:
# 给定如下二叉树，以及目标和 sum = 22，

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

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
    def pathSum(self, root: TreeNode, sum: int):
        # 回溯法
        result = []
        if not root:
            return result

        def backTrack(node, path, cur_sum):
            cur_sum += node.val
            path.append(node.val)
            if not node.left and not node.right:
                # 到达叶子结点
                if cur_sum == sum:
                    result.append(path[:])
            else:
                if not node.left:
                    backTrack(node.right, path, cur_sum)
                elif not node.right:
                    backTrack(node.left, path, cur_sum)
                else:
                    backTrack(node.left, path, cur_sum)
                    backTrack(node.right, path, cur_sum)
            path.pop()
            cur_sum -= node.val

        backTrack(root, [], 0)

        return result

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
    result = solution.pathSum(root, 9)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
