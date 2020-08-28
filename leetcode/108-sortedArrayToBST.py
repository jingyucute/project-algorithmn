'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 09:06:10
'''

# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 示例:

# 给定有序数组: [-10,-3,0,5,9],

# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sortedArrayToBST(self, nums) -> TreeNode:
        import random
        # 中序遍历

        def build(left, right):
            if left > right:
                return None
            # 序列中选择中间或左边的数为根
            # mid = (left + right) // 2
            # 序列中选择中间或右边的数为根
            # mid = (left + right + 1) // 2
            mid = (left + right + random.randint(0, 1)) // 2
            node = TreeNode(nums[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid+1, right)
            return node
        return build(0, len(nums)-1)

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

    nums = [-10, -3, 0, 5, 9]
    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.sortedArrayToBST(nums)
    print(solution.broadTravse(node))
    end_time = datetime.datetime.now()
    print(end_time-start_time)
