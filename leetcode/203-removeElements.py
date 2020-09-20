'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-20 16:49:09
'''

# 编写一个算法来判断一个数 n 是不是快乐数。

# 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

# 如果 n 是快乐数就返回 True ；不是，则返回 False 。

#  

# 示例：

# 输入：19
# 输出：true
# 解释：
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prenode = ListNode(-1)
        prenode.next = head

        pre, cur = prenode, head

        while cur:
            if cur.val != val:
                pre = pre.next
                cur = cur.next
            else:
                pre.next = cur.next
                cur = cur.next
        return prenode.next


if __name__ == '__main__':

    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(6)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(5)
    node7 = ListNode(6)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    start_time = datetime.datetime.now()
    solution = Solution()
    node = solution.removeElements(head, 6)
    while node:
        print(node.val)
        node = node.next
    end_time = datetime.datetime.now()
    print(end_time-start_time)
