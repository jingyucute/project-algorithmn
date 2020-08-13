'''
Description:
Author: jingyu
Date: 2020-08-10 11:43:25
LastEditors: Please set LastEditors
LastEditTime: 2020-08-14 00:33:09
'''

# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# 示例：

# 给定一个链表: 1->2->3->4->5, 和 n = 2.

# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：

# 给定的 n 保证是有效的。

# 进阶：

# 你能尝试使用一趟扫描实现吗？


import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    #   双指针, 其实更好的说法应该是固定宽度的窗口进行滑动
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        headNode = ListNode(0)
        headNode.next = head
        # second 指向倒数第n个结点的前一个结点
        # first 指向最后一个结点的后一个结点
        # first - second = n + 1
        first, second = headNode, headNode
        for i in range(n+1):
            first = first.next
        while first != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return headNode.next


if __name__ == '__main__':

    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.removeNthFromEnd(head, 2)
    while node != None:
        print(node.val)
        node = node.next
    end_time = datetime.datetime.now()
    print(end_time-start_time)
