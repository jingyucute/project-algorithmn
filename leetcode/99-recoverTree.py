'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-25 16:07:55
'''

# 二叉搜索树中的两个节点被错误地交换。

# 请在不改变其结构的情况下，恢复这棵树。

# 示例 1:

# 输入: [1,3,null,null,2]

#    1
#   /
#  3
#   \
#    2

# 输出: [3,1,null,null,2]

#    3
#   /
#  1
#   \
#    2
# 示例 2:

# 输入: [3,1,4,null,null,2]

#   3
#  / \
# 1   4
#    /
#   2

# 输出: [2,1,4,null,null,3]

#   2
#  / \
# 1   4
#    /
#   3
# 进阶:

# 使用 O(n) 空间复杂度的解法很容易实现。
# 你能想出一个只使用常数空间的解决方案吗？


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        def inorder(x):
            if not x:
                return []
            else:
                return inorder(x.left) + [x] + inorder(x.right)
        ol = inorder(root)
        sa = sorted(ol, key=lambda x: x.val)
        temp = [ol[i] for i in range(len(ol)) if ol[i].val != sa[i].val]
        temp[0].val, temp[1].val = temp[1].val, temp[0].val


if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.right = node1
    node1.left = node2
    start_time = datetime.datetime.now()
    solution = Solution()
    solution.recoverTree(root)

    end_time = datetime.datetime.now()
    print(end_time-start_time)
