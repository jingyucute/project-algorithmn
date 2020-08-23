'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-23 20:46:50
'''

# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

# 示例 1:

# 输入: 1->1->2
# 输出: 1->2
# 示例 2:

# 输入: 1->1->2->3->3
# 输出: 1->2->3


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prehead.next = head
        preNode = prehead
        curNode = head
        while curNode and curNode.next:
            if curNode.val == curNode.next.val:
                while curNode and curNode.next and curNode.val == curNode.next.val:
                    curNode = curNode.next
                preNode.next = curNode
            else:
                curNode = curNode.next
                preNode = preNode.next

        return prehead.next


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(4)
    node6 = ListNode(5)
    node7 = ListNode(5)
    node8 = ListNode(6)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.deleteDuplicates(head)
    while node:
        print(node.val)
        node = node.next
    end_time = datetime.datetime.now()
    print(end_time-start_time)
