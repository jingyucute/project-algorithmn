'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 13:09:27
'''

# 给出一个完全二叉树，求出该树的节点个数。

# 说明：

# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

# 示例:

# 输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# 输出: 6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-complete-tree-nodes
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

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left)+self.countNodes(root.right)


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
    result = solution.countNodes(root)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
