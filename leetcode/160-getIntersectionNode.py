'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-04 08:30:31
'''

# 编写一个程序，找到两个单链表相交的起始节点。

# 如下面的两个链表：


# 在节点 c1 开始相交。

#  

# 示例 1：


# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#  

# 示例 2：


# 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
#  

# 示例 3：


# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。
#  

# 注意：

# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。


#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        se = set()
        while headA:
            se.add(headA)
            headA = headA.next

        while headB:
            if headB in se:
                return headB
            headB = headB.next
        return None

    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 这个思路很有意思， 我过你来时的路
        # 走完各自的路, 再走对方的路, 这样双方走的长度会一样，故一定会相遇(没有交点，相遇在None)
        if not headA or not headB:
            return None
        nodeA = headA
        nodeB = headB
        while nodeA != nodeB:
            if nodeA:
                nodeA = nodeA.next
            else:
                nodeA = headB

            if nodeB:
                nodeB = nodeB.next
            else:
                nodeB = headA
        return nodeA


if __name__ == '__main__':

    headA = ListNode(4)
    node1 = ListNode(1)
    node2 = ListNode(8)
    node3 = ListNode(4)
    node4 = ListNode(5)
    headA.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    headB = ListNode(5)
    node5 = ListNode(0)
    node6 = ListNode(1)
    headB.next = node5
    node5.next = node6
    node6.next = node2

    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.getIntersectionNode1(headA, headB)
    while node:
        print(node.val)
        node = node.next
    end_time = datetime.datetime.now()
    print(end_time-start_time)