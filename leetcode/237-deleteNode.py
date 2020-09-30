'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-30 11:15:00
'''
# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。

#  

# 现有一个链表 -- head = [4,5,1,9]，它可以表示为:


#  

# 示例 1：

# 输入：head = [4,5,1,9], node = 5
# 输出：[4,1,9]
# 解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
# 示例 2：

# 输入：head = [4,5,1,9], node = 1
# 输出：[4,5,9]
# 解释：给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
#  

# 提示：

# 链表至少包含两个节点。
# 链表中所有节点的值都是唯一的。
# 给定的节点为非末尾节点并且一定是链表中的一个有效节点。
# 不要从你的函数中返回任何结果。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    head = ListNode(4)
    node2 = ListNode(5)
    node3 = ListNode(1)
    node4 = ListNode(9)
    head.next = node2
    node2.next = node3
    node3.next = node4
    solution = Solution()
    start_time = datetime.datetime.now()
    solution.deleteNode(head)
    node = head
    while node:
        print(node.val)
        node = node.next
    # print(result.val)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
