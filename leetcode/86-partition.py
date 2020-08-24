'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-24 18:09:46
'''

# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

# 你应当保留两个分区中每个节点的初始相对位置。

# 示例:

# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 拆分列表， 根据条件， 加入不同的链表末端
    def partition(self, head: ListNode, x: int) -> ListNode:
        beforeHead, afterHead = ListNode(-1), ListNode(-1)
        before, after = beforeHead, afterHead
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = afterHead.next

        return beforeHead.next


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(4)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node4 = ListNode(5)
    node5 = ListNode(2)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    x = 3
    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.partition(head, x)
    while node:
        print(node.val)
        node = node.next
    end_time = datetime.datetime.now()
    print(end_time-start_time)
