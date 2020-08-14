'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-14 18:17:23
'''


# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

# 示例:

# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        length = len(lists)

        def merge(left, right):
            preHead = ListNode(-1)
            preV = preHead
            while left and right:
                if left.val <= right.val:
                    preV.next = left
                    left = left.next
                else:
                    preV.next = right
                    right = right.next
                preV = preV.next

            if left:
                preV.next = left
            if right:
                preV.next = right

            return preHead.next

        def mergeList(low, high):
            if low == high:
                return lists[low]
            mid = (low + high) // 2
            left = mergeList(low, mid)
            right = mergeList(mid+1, high)
            return merge(left, right)

        if length <= 0:
            return None

        return mergeList(0, length - 1)


if __name__ == '__main__':

    head1 = ListNode(1)
    node1_2 = ListNode(4)
    node1_3 = ListNode(5)
    head1.next = node1_2
    node1_2.next = node1_3

    head2 = ListNode(1)
    node2_2 = ListNode(3)
    node2_3 = ListNode(4)
    head2.next = node2_2
    node2_2.next = node2_3

    head3 = ListNode(2)
    node3_2 = ListNode(6)
    head3.next = node3_2

    list = [head1, head2, head3]

    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.mergeKLists([])
    head = node
    while head != None:
        print(head.val)
        head = head.next

    end_time = datetime.datetime.now()
    print(end_time-start_time)
