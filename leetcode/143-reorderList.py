'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-03 08:35:49
'''

# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 示例 1:

# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 示例 2:

# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 我的想法是将链表结点放入数组中, 这样就可以实现随机访问
    # 也不知道方法合适不合适
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        ll = []
        cnode = head
        while cnode:
            ll.append(cnode)
            cnode = cnode.next
        length = len(ll)
        pnode = ListNode(-1)
        for i in range((length + 1) // 2):
            front = ll[i]
            tail = ll[length - 1 - i]
            # print(front.val, tail.val)
            if front != tail:
                front.next = tail
                pnode.next = front
                pnode = tail
            else:
                pnode.next = front
                pnode = front
        pnode.next = None


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

    start_time = datetime.datetime.now()
    solution = Solution()
    solution.reorderList(head)
    node = head
    while node:
        print(node.val)
        node = node.next
    end_time = datetime.datetime.now()
    print(end_time-start_time)
