'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 12:31:27
'''

# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

# 初始状态下，所有 next 指针都被设置为 NULL。

#  

# 示例：


# 输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

# 输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
#  

# 提示：

# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 层次遍历
        if not root:
            return None
        queue = []
        queue.append(root)
        while queue:
            length = len(queue)
            temp = []
            for i in range(length):
                node = queue[0]
                del queue[0]
                temp.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            for i in range(1, len(temp)):
                prev, cur = temp[i - 1], temp[i]
                prev.next = cur

        return root

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

    root = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node1_1 = Node(4)
    node1_2 = Node(5)
    node2_1 = Node(6)
    node2_2 = Node(7)
    root.left = node1
    root.right = node2
    node1.left = node1_1
    node1.right = node1_2
    node2.left = node2_1
    node2.right = node2_2

    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.connect(root)
    print(solution.broadTravse(node))
    end_time = datetime.datetime.now()
    print(end_time-start_time)
