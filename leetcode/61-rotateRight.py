'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 10:18:42
'''
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

# 示例 1:

# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:

# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        prehead = ListNode(-1)
        prehead.next = head

        # 形成闭环
        tail = prehead
        length = 0
        while tail.next:
            tail = tail.next
            length += 1

        tail.next = prehead.next

        k = length - k % length
        for _ in range(k):
            tail = tail.next
            prehead.next = prehead.next.next

        tail.next = None
        return prehead.next


if __name__ == '__main__':

    head = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    head.next = node1
    node1.next = node2
    k = 4
    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.rotateRight(head, k)
    while node:
        print(node.val)
        node = node.next
    end_time = datetime.datetime.now()
    print(end_time-start_time)
