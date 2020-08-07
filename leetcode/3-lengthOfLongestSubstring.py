'''
Description: 
Author: jingyu
Date: 2020-08-07 21:05:30
LastEditors: Please set LastEditors
LastEditTime: 2020-08-07 23:15:57
'''
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        str_len = len(s)
        str_set = set()  # 存放没有重复的字符
        left = 0
        cur_len = 0
        max_len = 0
        for i in range(str_len):
            cur_len += 1
            while s[i] in str_set:
                str_set.remove(s[left])  # 这个移除最左的字符， 也就是窗口滑动
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            str_set.add(s[i])
        return max_len


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    str = "aabbccde"
    s = Solution()
    print(str, s.lengthOfLongestSubstring(str))
    end_time = datetime.datetime.now()
    print(end_time-start_time)
