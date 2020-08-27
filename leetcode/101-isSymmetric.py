'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-27 18:52:02
'''

# 给定一个二叉树，检查它是否是镜像对称的。

#  

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  

# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

#     1
#    / \
#   2   2
#    \   \
#    3    3
#  

# 进阶：

# 你可以运用递归和迭代两种方法解决这个问题吗？

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
    def isSymmetric(self, root: TreeNode) -> bool:

        def travse(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                if travse(p.left, q.right) and travse(p.right, q.left):
                    return True
            return False
        return travse(root, root)

    def isSymmetric1(self, root: TreeNode) -> bool:

        def check(u, v):
            queue = []
            queue.append(u)
            queue.append(v)
            while queue:
                u = queue[0]
                del queue[0]
                v = queue[0]
                del queue[0]
                if not u and not v:
                    continue
                if (not u or not v) or u.val != v.val:
                    return False
                queue.append(u.left)
                queue.append(v.right)

                queue.append(u.right)
                queue.append(v.left)
            return True
        return check(root, root)


if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(2)
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
    result = solution.isSymmetric1(root)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
