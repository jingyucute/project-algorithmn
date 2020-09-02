'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-02 09:49:40
'''

# 给定一个链表，判断链表中是否有环。

# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

#  

# 示例 1：

# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。


# 示例 2：

# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。


# 示例 3：

# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。


#  

# 进阶：

# 你能用 O(1)（即，常量）内存解决此问题吗？

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        while head:
            if head in visited:
                return head
            else:
                visited.add(head)
                head = head.next
        return None


if __name__ == '__main__':

    head = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1

    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.detectCycle(head)
    print(node.val)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
