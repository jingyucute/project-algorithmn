'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-14 18:54:59
'''


# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

#  

# 示例:

# 给定 1->2->3->4, 你应该返回 2->1->4->3.


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 思路有点类似于双指针， 窗口滑动
        prehead = ListNode(-1)
        prehead.next = head

        first, second = prehead, prehead

        w = 0
        while w < 2 and first:
            first = first.next
            w += 1
        if w < 2:
            return head

        while first and second:
            # 处理结点交换
            t_node = second.next
            second.next = first
            t_node.next = first.next
            first.next = t_node
            first = t_node
            # 这里进行指针移动 判断
            if first.next and first.next.next:
                first = first.next.next
                second = second.next.next
            else:
                break

        return prehead.next

    def swapPairs1(self, head: ListNode) -> ListNode:
        # 官方递归算法
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs1(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node


if __name__ == '__main__':

    head1 = ListNode(1)
    node1_2 = ListNode(2)
    node1_3 = ListNode(3)
    # node1_4 = ListNode(4)
    head1.next = node1_2
    node1_2.next = node1_3
    # node1_3.next = node1_4

    # head2 = ListNode(1)
    # node2_2 = ListNode(3)
    # node2_3 = ListNode(4)
    # head2.next = node2_2
    # node2_2.next = node2_3

    # head3 = ListNode(2)
    # node3_2 = ListNode(6)
    # head3.next = node3_2

    # list = [head1, head2, head3]

    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.swapPairs(head1)
    head = node
    while head != None:
        print(head.val)
        head = head.next

    end_time = datetime.datetime.now()
    print(end_time-start_time)
