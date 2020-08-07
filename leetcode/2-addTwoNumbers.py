'''
Description: 
Author: jingyu
Date: 2020-08-07 18:28:11
LastEditors: Please set LastEditors
LastEditTime: 2020-08-07 19:20:01
'''
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        add_flag = 0

        node = None
        result_node = None
        while l1 != None and l2 != None:
            new_node = None
            if l1.val + l2.val + add_flag > 9:
                new_node = ListNode(l1.val + l2.val + add_flag - 10)
                add_flag = 1
            else:
                new_node = ListNode(l1.val + l2.val + add_flag)
                add_flag = 0
            if (node == None):
                node = new_node
                result_node = node
            else:
                node.next = new_node
                node = new_node
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            new_node = None
            if l1.val + add_flag > 9:
                new_node = ListNode(l1.val + add_flag - 10)
                add_flag = 1
            else:
                new_node = ListNode(l1.val + add_flag)
                add_flag = 0
            node.next = new_node
            node = node.next
            l1 = l1.next

        while l2 != None:
            new_node = None
            if l2.val + add_flag > 9:
                new_node = ListNode(l2.val + add_flag - 10)
                add_flag = 1
            else:
                new_node = ListNode(l2.val + add_flag)
                add_flag = 0
            node.next = new_node
            node = node.next
            l2 = l2.next

        if add_flag:
            new_node = ListNode(add_flag)
            node.next = new_node

        return result_node


if __name__ == '__main__':
    start_time = datetime.datetime.now()

    node1_1 = ListNode(8)
    node1_2 = ListNode(6)
    node1_3 = ListNode(3)
    node1_1.next = node1_2
    node1_2.next = node1_3

    node2_1 = ListNode(6)
    node2_2 = ListNode(4)
    node2_3 = ListNode(8)
    node2_1.next = node2_2
    node2_2.next = node2_3

    node1 = node1_1
    num1 = []
    while node1 != None:
        num1.append(node1.val)
        node1 = node1.next

    node2 = node2_1
    num2 = []
    while node2 != None:
        num2.append(node2.val)
        node2 = node2.next

    print(num1)
    print(num2)

    s = Solution()
    result_node = s.addTwoNumbers(node1_1, node2_1)
    reuslt_num = []
    result = result_node
    while result != None:
        reuslt_num.append(result.val)
        result = result.next
    print(reuslt_num)
    end_time = datetime.datetime.now()
    print(end_time-start_time)

# 我觉得这题有点儿 按序合并数组的味道
