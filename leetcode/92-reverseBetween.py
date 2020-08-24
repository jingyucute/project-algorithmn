'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-25 01:38:26
'''

# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。

# 示例:

# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prehead = ListNode(-1)
        prehead.next = head
        headNode, tailNode = head, head
        pre = prehead
        for i in range(n - 1):
            tailNode = tailNode.next
            if i < m - 1:
                headNode = headNode.next
                pre = pre.next

        def reverse(headNode, tailNode):
            prev = tailNode.next
            p = headNode
            while prev != tailNode:
                nex = p.next
                p.next = prev
                prev = p
                p = nex
            return tailNode, headNode

        nex = tailNode.next
        headNode, tailNode = reverse(headNode, tailNode)
        pre.next = headNode
        tailNode.next = nex

        return prehead.next

    # 官方递归
    def reverseBetween1(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head


if __name__ == '__main__':

    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    m = 2
    n = 4
    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.reverseBetween1(head, m, n)
    while node:
        print(node.val)
        node = node.next
    end_time = datetime.datetime.now()
    print(end_time-start_time)
