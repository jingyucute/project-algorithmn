'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 09:44:40
'''

# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 示例:

# 给定的有序链表： [-10, -3, 0, 5, 9],

# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

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

    # 看的官网的
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        #  最巧妙的部分, 就是寻找链表中中间的结点, 快慢指针
        def getMidNode(left, right):
            fast = slow = left
            while fast != right and fast.next != right:
                # 相当于slow = 1/2 * fast
                fast = fast.next.next
                slow = slow.next
            return slow

        def buildTree(left, right):
            if left == right:
                return None
            midNode = getMidNode(left, right)
            node = TreeNode(midNode.val)
            node.left = buildTree(left, midNode)
            node.right = buildTree(midNode.next, right)
            return node

        return buildTree(head, None)

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
    node = solution.sortedListToBST(head)
    print(solution.broadTravse(node))
    end_time = datetime.datetime.now()
    print(end_time-start_time)
