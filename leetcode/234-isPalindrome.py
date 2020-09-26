'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-09-26 18:18:41
'''

# 请判断一个链表是否为回文链表。

# 示例 1:

# 输入: 1->2
# 输出: false
# 示例 2:

# 输入: 1->2->2->1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#!user/bin/python
# _*_ coding: utf-8 _*_

import datetime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val = []
        curNode = head
        while curNode:
            val.append(curNode.val)
            curNode = curNode.next

        return val == val[::-1]


if __name__ == '__main__':
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    head.next = node2
    node2.next = node3
    node3.next = node4
    solution = Solution()
    start_time = datetime.datetime.now()
    result = solution.isPalindrome(head)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
