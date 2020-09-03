'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-03 16:22:47
'''

# 对链表进行插入排序。


# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

#  

# 插入排序算法：

# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#  

# 示例 1：

# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2：

# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left, right = self.sortList(head), self.sortList(mid)
        cur = prehead = ListNode(-1)
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return prehead.next


if __name__ == '__main__':

    head = ListNode(4)
    node1 = ListNode(2)
    node2 = ListNode(1)
    node3 = ListNode(5)
    node4 = ListNode(3)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.sortList(head)
    while node:
        print(node.val)
        node = node.next
    end_time = datetime.datetime.now()
    print(end_time-start_time)
