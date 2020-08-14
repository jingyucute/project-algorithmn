'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-15 06:58:29
'''


# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。

# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

#  

# 示例：

# 给你这个链表：1->2->3->4->5

# 当 k = 2 时，应当返回: 2->1->4->3->5

# 当 k = 3 时，应当返回: 3->2->1->4->5

#  

# 说明：

# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def revereList(head, tail):
            # 链表反转， 这里写的很巧妙
            # 将头一个结点插入，并指向规定的刚插入的结点, 这样就可以保证是逆序的
            prev = tail.next
            p = head
            while prev != tail:
                nex = p.next
                p.next = prev
                prev = p
                p = nex

            return tail, head

        prehead = ListNode(-1)
        prehead.next = head
        pre = prehead

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return prehead.next

            # 将部分链表和原来的链表进行链接， 不然指针的乱掉
            nex = tail.next
            head, tail = revereList(head, tail)
            tail.next = nex
            pre.next = head

            # 特定指针移动
            pre = tail
            head = tail.next

        return prehead.next


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
    node = solution.reverseKGroup(head1, 2)
    head = node
    while head != None:
        print(head.val)
        head = head.next

    end_time = datetime.datetime.now()
    print(end_time-start_time)
