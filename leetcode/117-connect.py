'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-28 12:45:35
'''

# 给定一个二叉树

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

# 初始状态下，所有 next 指针都被设置为 NULL。

#  

# 进阶：

# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
#  

# 示例：


# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
#  

# 提示：

# 树中的节点数小于 6000
# -100 <= node.val <= 100

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
            for i in range(length):
                node = queue[0]
                del queue[0]
                if i < length - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

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
