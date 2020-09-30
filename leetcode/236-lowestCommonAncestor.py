'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-30 10:52:49
'''

# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]


#  

# 示例 1:

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 示例 2:

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#  

# 说明:

# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = root

        def dfs(node):
            nonlocal ans
            if not node:
                return False
            lson = dfs(node.left)
            rson = dfs(node.right)
            if (lson and rson) or ((node.val == p.val or node.val == q.val) and (lson or rson)):
                ans = node
            return lson or rson or (node.val == p.val or node.val == q.val)

        dfs(root)

        return ans


if __name__ == '__main__':
    root = TreeNode(3)
    node2 = TreeNode(5)
    node3 = TreeNode(1)
    node4 = TreeNode(6)
    node5 = TreeNode(2)
    node6 = TreeNode(0)
    node7 = TreeNode(8)
    node8 = TreeNode(7)
    node9 = TreeNode(4)

    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node5.right = node9

    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.lowestCommonAncestor(root, node2, node9)
    print(result.val)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
