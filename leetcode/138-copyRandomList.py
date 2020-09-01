'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-01 14:37:23
'''

# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

# 要求返回这个链表的 深拷贝。 

# 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
#  

# 示例 1：


# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
# 示例 2：


# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
# 示例 3：


# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
# 示例 4：

# 输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
#  

# 提示：

# -10000 <= Node.val <= 10000
# Node.random 为空（null）或指向链表中的节点。
# 节点数目不超过 1000 。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}

        def dfs(node):
            if not node:
                return None
            if node in visited:
                return visited[node]

            newNode = Node(node.val, None, None)
            visited[node] = newNode

            newNode.next = dfs(node.next)
            newNode.random = dfs(node.random)

            return newNode

        return dfs(head)


if __name__ == '__main__':

    head = Node(7)
    node1 = Node(13)
    node2 = Node(11)
    node3 = Node(10)
    node4 = Node(1)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    head.random = None
    node1.random = head
    node2.random = node4
    node3.random = node2
    node4.random = head
    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.copyRandomList(head)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
