'''
Description: 
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-14 01:37:05
'''


# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

#  

# 示例：

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        headNode = ListNode(0)
        pNode = headNode
        p1 = l1
        p2 = l2
        while p1 != None and p2 != None:
            # print(p1.val, p2.val)
            if p1.val <= p2.val:
                node = ListNode(p1.val)
                pNode.next = node
                p1 = p1.next
                pNode = pNode.next
            else:
                node = ListNode(p2.val)
                pNode.next = node
                p2 = p2.next
                pNode = pNode.next
        while p1 != None:
            node = ListNode(p1.val)
            pNode.next = node
            p1 = p1.next
            pNode = pNode.next

        while p2 != None:
            node = ListNode(p2.val)
            pNode.next = node
            p2 = p2.next
            pNode = pNode.next

        return headNode.next

    #   官网写的， 自己多琢磨琢磨
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next

    # 递归写法
    def mergeTwoLists2(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2


if __name__ == '__main__':

    head1 = ListNode(1)
    node1_2 = ListNode(2)
    node1_3 = ListNode(4)
    head1.next = node1_2
    node1_2.next = node1_3

    head2 = ListNode(1)
    node2_2 = ListNode(3)
    node2_3 = ListNode(4)
    head2.next = node2_2
    node2_2.next = node2_3

    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.mergeTwoLists(head1, head2)
    head = node

    while head != None:
        print(head.val)
        head = head.next
    end_time = datetime.datetime.now()
    print(end_time-start_time)
