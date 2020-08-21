'''
Description:
Author: jingyu
Date: 2020-08-14 01:09:27
LastEditors: Please set LastEditors
LastEditTime: 2020-08-22 00:24:14
'''


# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

# 如果不存在最后一个单词，请返回 0 。

# 说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

#  

# 示例:

# 输入: "Hello World"
# 输出: 5


#!user/bin/python
# _*_ coding: utf-8 _*_
import datetime


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        return len(s.split(" ")[-1])


if __name__ == '__main__':
    s = "a "

    start_time = datetime.datetime.now()
    solution = Solution()
    result = solution.lengthOfLastWord(s)
    print(result)
    end_time = datetime.datetime.now()
    print(end_time-start_time)
