'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-20 11:09:30
'''

# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

#  

# 示例 1：

# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2：

# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#  

# 提示：

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400


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
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            result.append(queue[-1].val)
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue[:] = temp[:]
        return result

    #  深度优先

    def rightSideView1(self, root: TreeNode):
        if not root:
            return []

        result = []

        def dfs(node, depth):
            if node:
                if depth == len(result):
                    result.append(node.val)
                if node.right:
                    dfs(node.right, depth+1)
                if node.left:
                    dfs(node.left, depth+1)

        dfs(root, 0)

        return result


if __name__ == '__main__':

    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    root.left = node2
    root.right = node3
    node2.right = node5
    node3.left = node4

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.rightSideView1(root)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
