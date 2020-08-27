'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 00:45:08
'''

# 根据一棵树的前序遍历与中序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 例如，给出

# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：

#     3
#    / \
#   9  20
#     /  \
#    15   7

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
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder:
            return None
        node_val = preorder[0]
        node_index = inorder.index(node_val)
        node_left = self.buildTree(
            preorder[1:1+node_index], inorder[0:node_index])
        node_right = self.buildTree(
            preorder[node_index+1:], inorder[node_index+1:])
        node = TreeNode(node_val)
        node.left = node_left
        node.right = node_right
        return node

    # 官方递归, 与我的区别主要在于， 确定区间是利用 下表， 我的是改变 list
    def buildTree1(self, preorder, inorder) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(
                preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(
                preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

    # 迭代 copy 官方的
    def buildTree2(self, preorder, inorder) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                # 判断当前元素是否和中序遍历的元素相等, 也就是找 root
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)

        return root


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

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    start_time = datetime.datetime.now()
    solution = Solution()
    root = solution.buildTree2(preorder, inorder)
    print(root.val)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
